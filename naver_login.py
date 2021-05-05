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
