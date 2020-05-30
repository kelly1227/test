import selenium
from time import sleep
from selenium import webdriver

driver = webdriver.Safari()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('手机')
driver.find_element_by_id('su').click()
sleep(300)
driver.quit()