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

                    driver.get("https://lms.sunmoon.ac.kr/ilos/st/course/submain_form.acl")
                    time.sleep(3)
            # reload
            driver.get("https://lms.sunmoon.ac.kr/ilos/main/main_form.acl")
            time.sleep(1)

    print("All data : {}".format(data_lst))
    return data_lst