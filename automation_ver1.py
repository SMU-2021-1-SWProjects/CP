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

#browser시작
DRIVER_PATH = "" #chromedrive가 저장되어 있는 파일의 위치 입력
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
    pyperclip.copy(list_data2[1]) #1. 먼저. 
    print('checking now... ', list_data2[1])
    due_time.send_keys(Keys.COMMAND, 'a') #2. 나중에. 순서가 영향을 미친다... 
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
