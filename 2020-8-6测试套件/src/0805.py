import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()
driver.get("http://baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("韦德")
su1=driver.find_element_by_id("su")
#driver.find_element_by_id("su").click()

elem1=driver.find_element_by_link_text("https://www.hao123.com")
ActionChains(driver).move_to_element(elem1).perform()
time.sleep(5)
#右击
ActionChains(driver).context_click(su1).perform()
time.sleep(2)
#双击
ActionChains(driver).double_click(su1).perform()
time.sleep(5)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)
driver.find_element_by_id("kw").send_keys("詹姆斯")
driver.find_element_by_id("su").click()
'''禅道 Tab,Enter
driver.find_element_by_id("zentaobiz").click()

driver.find_element_by_id("account").send_keys("admin")
time.sleep(3)
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(3)
driver.find_element_by_name("password").send_keys("Gfc98@1115")
#driver.find_element_by_id("submit").click()
driver.find_element_by_name("password").send_keys(Keys.ENTER)
'''
'''
title=driver.title
print("title="+title)
driver.implicitly_wait(10)
driver.find_element_by_link_text(u"乃万_百度百科").click()
driver.maximize_window()

time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()


title2=driver.title
print("title="+title2)
#print(driver.current_url)
driver.set_window_size(400,400)
'''
time.sleep(6)
driver.quit()
