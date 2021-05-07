from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pyperclip
from datetime import datetime, date
import datetime


# browser시작
DRIVER_PATH = ""  # chromedrive가 저장되어 있는 파일의 위치 입력
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

def e_Login(driver):
    driver.get('https://lms.sunmoon.ac.kr/ilos/main/member/login_form.acl')

    # 3. 要素を探して操作する
    # 3-1. login
    id_elem = driver.find_element_by_css_selector("#usr_id")
    pyperclip.copy('whdhks455')
    id_elem.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    pass_elem = driver.find_element_by_css_selector("#usr_pwd")
    pyperclip.copy('dhksrl455!')
    pass_elem.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    login_elem = driver.find_element_by_css_selector("#myform > div > div > div > fieldset > input.btntype")
    login_elem.click()
    time.sleep(1)

    # changing language
    bar = driver.find_element_by_css_selector("#LANG")
    bar.click()
    language = driver.find_element_by_xpath('//option[@value="ko"]')
    language.click()

def data_extraction(driver):
    data_lst = []

    subjects = driver.find_elements_by_class_name('sub_open')

    dt_now = datetime.datetime.now()
    current_month = dt_now.month
    current_day = dt_now.day

    for i in range(len(subjects)):
        subjects = driver.find_elements_by_class_name('sub_open')
        subjects[i].click()
        time.sleep(1)
        try:
            driver.find_element_by_id('menu_report').click()
            time.sleep(1)

            assignments_num = driver.find_element_by_css_selector("#report_list > table > tbody > tr:nth-child(1) > td:nth-child(1)").text
            if assignments_num != "조회할 자료가 없습니다":
                assignments_num = int(assignments_num)
                for j in range(assignments_num):
                    assignment_data = []
                    assignments = driver.find_elements_by_class_name('subjt_top')
                    assignments[j].click()
                    time.sleep(1)
                    texts = driver.find_element_by_id("content_text")
                    trs = texts.find_elements(By.TAG_NAME, "tr")

                    # publication date
                    publication_date = trs[2].find_element(By.TAG_NAME, "td").text

                    lst = publication_date.split(" ")
                    publication_lst = lst[0]
                    publication_date_lst = publication_lst.split(".")
                    publication_month = int(publication_date_lst[1])
                    publication_day = int(publication_date_lst[2])
                    if publication_month == current_month and publication_day == current_day:
                        subject_name = driver.find_element_by_xpath("//*[@id='content_location']/div/a[2]").text
                        assignment_name = trs[0].find_element(By.TAG_NAME, "td").text
                        title = subject_name + " + " + assignment_name
                        assignment_data.append(title)
                        assignment_data.append(trs[2].find_element(By.TAG_NAME, "td").text)
                        assignment_data.append(trs[3].find_element(By.TAG_NAME, "td").text)
                        data_lst.append(assignment_data)
                    driver.find_element_by_id('menu_report').click()
                    time.sleep(1)
            # reload
            driver.get("https://lms.sunmoon.ac.kr/ilos/main/main_form.acl")
            time.sleep(1)

        except NoSuchElementException:
            icon_nums = driver.find_elements_by_class_name('chapter_content_icon')
            elems = driver.find_elements_by_class_name('chapter_content_title_wrap')

            for i in range(len(icon_nums)):
                elems = driver.find_elements_by_class_name('chapter_content_title_wrap')
                title = elems[i].find_element_by_tag_name('img').get_attribute('title')
                if title == "과제":
                    assignment_data = []
                    elems[i].click()
                    time.sleep(1)
                    texts = driver.find_element_by_id("content_text")
                    trs = texts.find_elements(By.TAG_NAME, "tr")

                    subject_name = driver.find_element_by_xpath("//*[@id='online_mode_lect_nm']/span/span[1]").text
                    assignment_name = trs[0].find_element(By.TAG_NAME, "td").text
                    title = subject_name + " + " + assignment_name
                    assignment_data.append(title)
                    assignment_data.append(trs[3].find_element(By.TAG_NAME, "td").text)
                    assignment_data.append(trs[2].find_element(By.TAG_NAME, "td").text)
                    print("Assignment Data: {}".format(assignment_data))
                    data_lst.append(assignment_data)

                    driver.get("https://lms.sunmoon.ac.kr/ilos/st/course/submain_form.acl")
                    time.sleep(3)
            # reload
            driver.get("https://lms.sunmoon.ac.kr/ilos/main/main_form.acl")
            time.sleep(1)

    print("All data : {}".format(data_lst))
    return data_lst

def login_naver(driver):
    driver.get("https://calendar.naver.com")
    tag_id = driver.find_element_by_css_selector('#id')
    tag_id.click()
    pyperclip.copy('id')
    tag_id.send_keys(Keys.COMMAND, 'v')
    time.sleep(1)

    tag_pw = driver.find_element_by_css_selector('#pw')
    tag_pw.click()
    pyperclip.copy('pw')
    tag_pw.send_keys(Keys.COMMAND, 'v')
    time.sleep(1)

    login_btn = driver.find_element_by_css_selector('#log\.login')
    login_btn.click()
    time.sleep(3)

# gwonin branch
def insert_due_date():
    # due date
    calendar_end_date = driver.find_element_by_xpath('//*[@id="end_date"]')
    time.sleep(2)
    driver.execute_script("arguments[0].click();", calendar_end_date)
    time.sleep(2)
    # calendar_end_date.click()
    pyperclip.copy(list_data2[0])

    calendar_end_date.send_keys(Keys.COMMAND, 'a')
    time.sleep(2)
    calendar_end_date.send_keys(Keys.COMMAND, 'v')

    time.sleep(2)
    calendar_start_date = driver.find_element_by_xpath('//*[@id="start_date"]')
    time.sleep(2)
    driver.execute_script("arguments[0].click();", calendar_start_date)

# gwonin branch
def insert_due_time():
    # due time
    due_time = driver.find_element_by_xpath(
        '//*[@id="_real_schedule_body"]/div[2]/div/div[4]/div[3]/div/div[5]/div[1]/input')
    driver.execute_script("arguments[0].click();", due_time)
    time.sleep(2)
    pyperclip.copy(list_data2[1])  # 1. 먼저.
    print('checking now... ', list_data2[1])
    due_time.send_keys(Keys.COMMAND, 'a')  # 2. 나중에. 순서가 영향을 미친다...
    due_time.send_keys(Keys.COMMAND, 'v')
    time.sleep(2)

    time.sleep(2)
    calendar_start_date = driver.find_element_by_xpath('//*[@id="start_date"]')
    time.sleep(2)
    driver.execute_script("arguments[0].click();", calendar_start_date)

    # calendar_start_date.click()

    temp1 = driver.find_element_by_css_selector(
        "#_real_schedule_body > div.schedule_header > div > button.save._save_btn._save")
    time.sleep(2)
    driver.execute_script("arguments[0].click();", temp1)
    temp1.click()
