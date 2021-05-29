from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import pyperclip
import datetime
import pymysql


def send_text(text, url):
    slack_url = url
    data = json.dumps({
        'username': 'auto-add-to-naver-calendar',
        'text': text,
    })
    requests.post(slack_url, data=data)

def get_driver():
    # options = webdriver.ChromeOptions()
    options = Options()
    options.add_argument('--disable-gpu');
    options.add_argument('--disable-extensions');
    options.add_argument('--proxy-server="direct://"');
    options.add_argument('--proxy-bypass-list=*');
    options.add_argument('--start-maximized');
    options.add_argument('--kiosk')
    options.add_experimental_option("excludeSwitches", ['enable-automation'])

    DRIVER_PATH = "chomedriver path"
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

    return driver

def login_sunmoon(driver, eid, epw):
    driver.get("https://lms.sunmoon.ac.kr/ilos/main/member/login_form.acl")
    time.sleep(1)

    id = driver.find_element_by_id('usr_id')
    id.send_keys(eid)

    pw = driver.find_element_by_id('usr_pwd')
    pw.send_keys(epw)

    driver.find_element_by_class_name('btntype').click()
    time.sleep(1)


def login_naver(driver, nid, npw):
    driver.get("https://calendar.naver.com")
    tag_id = driver.find_element_by_css_selector('#id')
    tag_id.click()
    pyperclip.copy(nid)
    tag_id.send_keys(Keys.COMMAND, 'v')
    time.sleep(1)

    tag_pw = driver.find_element_by_css_selector('#pw')
    tag_pw.click()
    pyperclip.copy(npw)
    tag_pw.send_keys(Keys.COMMAND, 'v')
    time.sleep(1)

    login_btn = driver.find_element_by_css_selector('#log\.login')
    login_btn.click()
    time.sleep(3)

def data_extraction(driver):
    data_lst = []

    subjects = driver.find_elements_by_class_name('sub_open')

    dt_now = datetime.datetime.now()
    current_month = dt_now.month
    current_day = dt_now.day

    # for i in range(len(subjects)):
    for i in range(1):
        subjects = driver.find_elements_by_class_name('sub_open')
        subjects[i].click()
        time.sleep(1)
        try:
            driver.find_element_by_id('menu_report').click()
            time.sleep(1)

            assignments_num = driver.find_element_by_css_selector(
                "#report_list > table > tbody > tr:nth-child(1) > td:nth-child(1)").text
            if assignments_num != "조회할 자료가 없습니다":
                assignments_num = int(assignments_num)
                for j in range(assignments_num):
                    assignment_data = []
                    assignments = driver.find_elements_by_class_name(
                        'subjt_top')
                    assignments[j].click()
                    time.sleep(1)
                    texts = driver.find_element_by_id("content_text")
                    trs = texts.find_elements(By.TAG_NAME, "tr")

                    # publication date
                    publication_date = trs[2].find_element(
                        By.TAG_NAME, "td").text

                    subject_name = driver.find_element_by_xpath(
                        "//*[@id='content_location']/div/a[2]").text
                    assignment_name = trs[0].find_element(
                        By.TAG_NAME, "td").text
                    title = subject_name + " + " + assignment_name
                    assignment_data.append(title)
                    assignment_data.append(
                        trs[2].find_element(By.TAG_NAME, "td").text)
                    assignment_data.append(
                        trs[3].find_element(By.TAG_NAME, "td").text)
                    data_lst.append(assignment_data)
                    driver.find_element_by_id('menu_report').click()
                    time.sleep(1)
            # reload
            driver.get("https://lms.sunmoon.ac.kr/ilos/main/main_form.acl")
            time.sleep(1)

        except NoSuchElementException:
            icon_nums = driver.find_elements_by_class_name(
                'chapter_content_icon')
            print("icon nums: {}".format(len(icon_nums)))
            elems = driver.find_elements_by_class_name(
                'chapter_content_title_wrap')
            print("elems: {}".format(len(elems)))

            for i in range(len(icon_nums)):
                elems = driver.find_elements_by_class_name(
                    'chapter_content_title_wrap')
                print("{}回目".format(i+1))
                title = elems[i].find_element_by_tag_name(
                    'img').get_attribute('title')
                if title == "과제":
                    assignment_data = []
                    print("{}番目のオブジェクト".format(i+1))
                    elems[i].click()
                    time.sleep(1)
                    texts = driver.find_element_by_id("content_text")
                    trs = texts.find_elements(By.TAG_NAME, "tr")

                    subject_name = driver.find_element_by_xpath(
                        "//*[@id='online_mode_lect_nm']/span/span[1]").text
                    assignment_name = trs[0].find_element(
                        By.TAG_NAME, "td").text
                    title = subject_name + " + " + assignment_name
                    assignment_data.append(title)
                    assignment_data.append(
                        trs[3].find_element(By.TAG_NAME, "td").text)
                    assignment_data.append(
                        trs[2].find_element(By.TAG_NAME, "td").text)
                    print("Assignment Data: {}".format(assignment_data))
                    data_lst.append(assignment_data)

                    driver.get(
                        "https://lms.sunmoon.ac.kr/ilos/st/course/submain_form.acl")
                    time.sleep(3)
            # reload
            driver.get("https://lms.sunmoon.ac.kr/ilos/main/main_form.acl")
            time.sleep(1)

    print("All data : {}".format(data_lst))
    return data_lst


def add_calendar(driver, data_lst):
    for data in data_lst:
        # 일정
        # driver.find_element_by_xpath('//*[@id="nav_snb"]/div/div[1]/a[1]').click()
        # driver.find_element_by_css_selector("#nav_snb > div > div.btn_workset > a.write_schedule > span").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="nav_snb"]/div/div[1]/a[1]').click()
        print('ok')
        time.sleep(3)

        # 제목
        calendar_title = driver.find_element_by_xpath('//*[@id="tx0_0"]')
        calendar_title.click()
        pyperclip.copy(data[0])
        calendar_title.send_keys(Keys.COMMAND, 'v')
        time.sleep(3)

        # due data
        lst2 = data[2].split(' ', 1)

        # due date
        calendar_end_date = driver.find_element_by_xpath('//*[@id="end_date"]')
        driver.execute_script("arguments[0].click();", calendar_end_date)
        calendar_end_date.click()
        pyperclip.copy(lst2[0])
        calendar_end_date.send_keys(Keys.COMMAND, 'a')
        time.sleep(3)
        calendar_end_date.send_keys(Keys.COMMAND, 'v')
        time.sleep(2)

        # due time
        due_time = driver.find_element_by_xpath(
            '//*[@id="_real_schedule_body"]/div[2]/div/div[4]/div[3]/div/div[5]/div[1]/input')
        driver.execute_script("arguments[0].click();", due_time)
        due_time.send_keys(Keys.COMMAND, 'a')
        time.sleep(3)
        pyperclip.copy(lst2[1])
        due_time.send_keys(Keys.COMMAND, 'v')
        time.sleep(3)

        calendar_start_date = driver.find_element_by_xpath(
            '//*[@id="start_date"]')
        driver.execute_script("arguments[0].click();", calendar_start_date)
        calendar_start_date.click()

        # 저장-button
        # css ver
        temp1 = driver.find_element_by_css_selector(
            "#_real_schedule_body > div.schedule_header > div > button.save._save_btn._save")
        driver.execute_script("arguments[0].click();", temp1)
        time.sleep(3)

        # reload
        driver.get("https://calendar.naver.com")
        time.sleep(2)


def main():
    #options = Options()
    options = webdriver.ChromeOptions()
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--proxy-server="direct://"')
    options.add_argument('--proxy-bypass-list=*')
    options.add_argument('--start-maximized')
    # options.add_argument('--kiosk') #window最大
    # chrome は自動テスト ソフトウェアによって制御されています
    options.add_experimental_option("excludeSwitches", ['enable-automation'])

    DRIVER_PATH = "/Users/ritsushi/Documents/chomedriver/chromedriver_ver90.0.4430.24"
    driver = webdriver.Chrome(
        executable_path=DRIVER_PATH, chrome_options=options)

    # login_sunmoon(driver)
    # data = data_extraction(driver)
    # # login_naver(driver)
    # # add_calendar(driver, data)
    # driver.close()
    # driver.quit()
    database(driver)
    print("driver stop")


if __name__ == "__main__":
    main()
