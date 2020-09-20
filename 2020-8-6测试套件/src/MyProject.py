import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()
driver.get("http://localhost:8080/ses/public/index.html")
driver.find_element_by_name("username").send_keys("abc")
driver.find_element_by_name("password").send_keys("123")
#driver.find_element_by_id("btn_to_register").click()

driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()

time.sleep(10);
driver.quit()