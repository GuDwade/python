from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class stu_exam_sys(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/ses/public/index.html"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(3)
        driver.find_element_by_name("username").send_keys("abc")
        driver.find_element_by_name("password").send_keys("123")
        driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("exam_record_tab").click()
        time.sleep(5)

    def test_update(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(2)
        driver.find_element_by_name("username").send_keys("abc")
        driver.find_element_by_name("password").send_keys("123")
        driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()
        time.sleep(2)
        driver.find_element_by_id("exam_record_tab").click()
        self.assertEqual(123,1234,"not equal")
        time.sleep(2)



    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)