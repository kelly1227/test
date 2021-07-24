from time import sleep
from appium import webdriver
import time
import random
import subprocess
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = 'SM-G977N'
desired_caps['appPackage'] = 'com.kuaishou.nebula'#com.taobao.taobao  com.jingdong.app.mall
desired_caps['appActivity'] = 'com.yxcorp.gifshow.HomeActivity' #com.taobao.tao.TBMainActivity  main.MainFrameActivity

class lianjia_auto_iphone():
    def adb_exceute(self,common):
        order_execute = subprocess.Popen(common, shell=True, stdout=subprocess.PIPE)
        result = order_execute.stdout.read()
        print("命令：",common,"\n 结果:",result)
        return result

    def adb_common(self):
        adb_devices = 'adb devices'  # 获取连接设备
        adb_am_list_package = 'adb shell pm list packages'
        self.adb_exceute(adb_devices)
        result = self.adb_exceute(adb_am_list_package)
        result_str = str(result)
        print("settings=",result_str.find("io.appium.settings"))
        print("unloack=",result_str.find("io.appium.unlock"))
        if result_str.find("package:io.appium.settings") != -1:
            adb_remove_apk = 'adb uninstall io.appium.settings'
            self.adb_exceute(adb_remove_apk)
        if result_str.find("package:io.appium.unlock") != -1:
            adb_remove_apk_1 = 'adb uninstall io.appium.unlock'
            self.adb_exceute(adb_remove_apk_1)
        # print(temp_list)
        adb_kill_server='adb kill-server'
        self.adb_exceute(adb_kill_server)


    def __init__(self):
        self.adb_common()
        time.sleep(10)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.randomint = random.randint(10,23)
        time.sleep(self.randomint)

    def uninstall_default_apk(self):
        app_setting = self.driver.is_app_installed("io.appium.settings")
        if app_setting:
            self.driver.remove_app("io.appium.settings")
        app_unlock = self.driver.is_app_installed("io.appium.unlock")
        if app_unlock:
            self.driver.remove_app("io.appium.unlock")

    def login_business(self):
        # 登录按钮
        element_login = self.driver.find_element_by_id("login_text")
        element_login.click()
        time.sleep(1)

        # 其他登录方式按钮  13122395209 #Aa12341234
        # element_other_login = driver.find_element_by_id("other_login_tv")
        # element_other_login.click()
        # time.sleep(1)

        # 点击密码登录
        element_pwd_login = self.driver.find_element_by_name("密码登录")
        element_pwd_login.click()
        time.sleep(1)

        # 用户名
        element_user_name = self.driver.find_element_by_id("phone_et")
        element_user_name.send_keys("13122395209")
        time.sleep(1)

        # 密码
        element_pwd_txt = self.driver.find_element_by_id("password_et")
        element_pwd_txt.send_keys("Aa12341234")
        time.sleep(1)

        # 登记登录
        element_login_btn = self.driver.find_element_by_id("confirm_btn")
        element_login_btn.click()
        time.sleep(1)

        # 登录按钮
        element_login = self.driver.find_element_by_id("login_text")
        element_login.click()
        time.sleep(1)
    # 滑动
    def task_list(self):
        # 登录按钮
        random_1 = random.randint(900,1000)
        random_2 = random.randint(1000,1200)
        random_time = random.randint(100,200)
        random_sleep_time = random.randint(50, 80)
        print(random_1,random_2,random_time,random_sleep_time)
        self.driver.swipe(100,random_1,100,random_2,random_time)
        time.sleep(12)
        print("停留多少秒：",random_sleep_time,random_1,random_2,"滑动屏幕时间",random_time)




if __name__ == '__main__':
    auto=lianjia_auto_iphone()
    # auto.adb_common()
    for index in range(1500):
        print("开始运行---",index)
        auto.task_list()
        print("结束一次--：",index)
