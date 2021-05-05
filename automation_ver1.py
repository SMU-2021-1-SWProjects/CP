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
    pass
