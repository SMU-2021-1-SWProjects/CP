#캘린더 제목란에 과제명 작성 코드



#데이터 추출 메서드(과제명)
def title_extract():
    list1 = []
    for i in range(len(list1)):
        driver.find_elements_by_css_selector('.sub_open')[i].click()
        try:
            driver.find_element_by_id('st_report').click()
            list2 = driver.find_elements_by_css_selector('.subjt_top')
            for j in range(len(list2)):
                driver.find_elements_by_css_selector('.subjt_top')[j].click()
                time.sleep(3)
                date1 = driver.find_element_by_css_selector(
                    '#content_text > table > tbody > tr:nth-child(1) > td').text
                date2 = driver.find_element_by_css_selector(
                    '#content_text > table > tbody > tr:nth-child(3) > td').text
                date3 = driver.find_element_by_css_selector(
                    '#content_text > table > tbody > tr:nth-child(4) > td').text
                print(date1, date2, date3)
                driver.find_element_by_css_selector('.site_button').click()

        except:
            pass

    driver.find_element_by_id('logo_link').click()
    list_end = []
    list_end.append(date1 + "," + date2 + "," + date3)
    print(len(list_end))

    for i in range(len(list_end)):
        print(list_end[i])

#캘린더 제목란에 저장하는 메서드
def save_title():
    list_end=[]
    for i in range(len(list_end)):
        if i != 0:
            driver.get("https://calendar.naver.com")
            print('ss')
        else:
            pass
        list_data = list_end[i].split(",")
        list_data0 = list_data[0]  # 제목

    #calendar title부분에 자동 저장
    calendar_title = driver.find_element_by_xpath('//*[@id="tx0_0"]')

    time.sleep(2)
    driver.execute_script("arguments[0].click();", calendar_title)

    pyperclip.copy(list_data0)
    calendar_title.send_keys(Keys.CONTROL, 'v')
