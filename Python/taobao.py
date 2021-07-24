from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'MI_4LTE'
desired_caps['appPackage'] = 'com.jingdong.app.mall'
desired_caps['appActivity'] = '.MainFrameActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver,timeout=60)
