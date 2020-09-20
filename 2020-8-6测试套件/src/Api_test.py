from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
'''
#time.sleep(5)
driver.implicitly_wait(5)
#title url
title=driver.title
url=driver.current_url
print("title:"+title)
print("url:"+url)
#设置窗口
driver.maximize_window()
time.sleep(3)
driver.set_window_size(400,400)
'''
driver.find_element_by_id("kw").send_keys("顾城")
driver.find_element_by_id("su").click()
time.sleep(5)

#前进 后退
driver.back();
time.sleep(5)
driver.forward()
time.sleep(5)

driver.quit()