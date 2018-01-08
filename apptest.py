# coding=utf-8
import time
from appium import webdriver
import time
import os




PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps = {

                'platformName': 'Android',

                'deviceName': 'H6TSPZIR95HAQWJR',

                # 'app' : PATH(r"C:\Users\chufusheng\Desktop\MaterialLoginExample.apk"),

                'platformVersion': '5.1',

                'appPackage': 'com.sourcey.materialloginexample',
                'appActivity' : 'com.sourcey.materiallogindemo.LoginActivity'

                # 'appActivity': 'com.taobao.tao.welcome.Welcome',

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id('com.sourcey.materialloginexample:id/input_email').send_keys('aasoligj')
# driver.findElement(By.id("com.sourcey.materialloginexample:id/input_email")).sendKeys("jack")
