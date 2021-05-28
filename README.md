# react native 실행 환경에 필요한 package입니다.

"dependencies": {

    "@react-native-community/masked-view": "0.1.10",
    "@react-navigation/native": "^5.9.4",
    "@react-navigation/stack": "^5.14.4",
    "axios": "^0.21.1",
    "body-parser": "^1.19.0",
    "bootstrap": "^5.0.0",
    "cors": "^2.8.5",

    "express": "^4.17.1",
    "formik": "^2.2.6",
    "mysql": "^2.18.1",
    "mysql2": "^2.2.5",
    "nodemon": "^2.0.7",
    
    "react-native-gesture-handler": "~1.10.2",
    "react-native-my-sql-connection": "^1.0.4",
    "react-native-reanimated": "~2.1.0",
    "react-native-safe-area-context": "3.2.0",
    "react-native-screens": "~3.0.0",
    "react-native-web": "~0.13.12",
    "react-router-dom": "^5.2.0",
    "sequelize": "^6.6.2",
    "tcomb-form-native": "^0.6.20"
}

# python Selenium 설치 방법입니다.

    Install
    일반 python 환경이라면 pip(pip3)을, conda 환경이라면 conda를 사용합니다.

    pip install selenium
    conda install selenium
    일반적인 파이썬 라이브러리와는 다르게, 하나 더 필요한 것이 있습니다.

    브라우저별로 selenium webdriver를 다운로드해야 한다. 저희는 크롬을 사용했습니다.

    Google Chrome
    버전이 여러 개가 있는데, 본인이 사용하는 Chrome의 버전에 맞는 webdriver를 다운받아야 합니다.
    크롬의 버전은 오른쪽 위 점 3개 > 도움말 > Chrome 정보에서 확인할 수 있습니다.

    다운받은 파일을 Python 파일과 같은 디렉토리에 둡니다. 
    다른 곳에 두어도 상관없지만, driver 경로를 입력하기 편하게 하기 위해서 입니다.

    Import
    
    import selenium
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support.ui import WebDriverWait
    
    
    추가적인 Selenium 사용법은 https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/ 참고
