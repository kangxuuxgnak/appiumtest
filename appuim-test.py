from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

import time
import os


def until(x):
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(x)).click()
    # driver.find_element_by_id(x).click()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

desired_caps = {}
desired_caps['deviceName'] = 'xxxxxxxxx'
desired_caps['platformName'] = 'Android'
desired_caps['version'] = '10'
desired_caps['appPackage'] = 'com.microsoft.bing'
desired_caps['appActivity'] = 'com.microsoft.clients.bing.app.MainActivity'
# desired_caps['unicodeKeyboard'] = Ture
# desired_caps['resetKeyboard'] = Ture

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# driver.start_activity('com.zhihu.android', 'com.zhihu.android.app.ui.activity.LauncherActivity')
# print(driver.page_source)
# driver.background_app(5)

until("com.microsoft.bing:id/skip_text")
until("com.android.permissioncontroller:id/permission_allow_always_button")
until("com.android.permissioncontroller:id/permission_allow_button")
until("com.microsoft.bing:id/search_box")
time.sleep(2)
driver.find_element_by_id("com.microsoft.bing:id/search_text_field").send_keys("123")

# os.system('adb shell input tap 1000 2200')

TouchAction(driver).tap(x=1000, y=2200).perform()

i = 3
for i in range(1, 3):
    driver.swipe(500, 1700, 500, 500)

print(driver.get_window_size()["width"])
print(driver.get_window_size()["height"])
print(driver.device_time)

i = 3
for i in range(1, 3):
    driver.keyevent(24)


driver.open_notifications()
