import pymysql


def database(driver):
    conn = pymysql.connect(host='localhost', user='root',
                           password='mysql_76', db='react_native', charset='utf8')

    try:
        with conn.cursor() as curs:
            sql = "SELECT * FROM react_native.id_pw;"
            curs.execute(sql)  # 실행할 sql문 넣기
            rs = curs.fetchall()  # sql문 실행해서 데이터 가져오기
        for i in range(len(rs)):
            e_id = rs[i][1]
            e_pw = rs[i][2]
            n_id = rs[i][3]
            n_pw = rs[i][4]

            options = webdriver.ChromeOptions()
            options = Options()
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-extensions')
            options.add_argument('--proxy-server="direct://"')
            options.add_argument('--proxy-bypass-list=*')
            options.add_argument('--start-maximized')
            options.add_experimental_option(
                "excludeSwitches", ['enable-automation'])

            DRIVER_PATH = "/Users/ritsushi/Documents/chomedriver/chromedriver_ver90.0.4430.24"
            driver = webdriver.Chrome(
                executable_path=DRIVER_PATH, chrome_options=options)

            login_sunmoon(driver, e_id, e_pw)
            data = data_extraction(driver)
            login_naver(driver, n_id, n_pw)
            add_calendar(driver, data)

            driver.close()
            driver.quit()
    finally:
        conn.close()
