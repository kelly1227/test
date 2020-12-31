from time import sleep
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'MI_4LTE'
desired_caps['appPackage'] = 'com.jingdong.app.mall'#com.taobao.taobao  com.jingdong.app.mall
desired_caps['appActivity'] = '.main.MainActivity' #com.taobao.tao.TBMainActivity  main.MainFrameActivity

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver,30)

login = driver.find_element_by_xpath("//android.view.View[@content-desc='我的']")
wait = WebDriverWait(driver,20)

login = driver.find_element_by_xpath("//android.view.View[@content-desc='我的']")
wait = WebDriverWait(driver,20)