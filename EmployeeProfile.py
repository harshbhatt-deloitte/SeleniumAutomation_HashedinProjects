import time
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from AdminLogin import Login
import unittest


class AddEmployee(Login):
    def __init__(self):
        super().__init__()

    def employee(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-profile']").click()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-profile']").is_displayed()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Mark")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("mark101")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("qwerty")
        self.driver.find_element(By.XPATH, "//select[@name='roles']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//option[@value='user']").click()
        self.driver.find_element(By.XPATH, "//input[@name='skills_input']").send_keys("java")
        time.sleep(5)
        self.driver.find_elements(By.XPATH, "//select[@name='designation']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//option[text()='Backend']").click()
        self.driver.find_element(By.XPATH, "//select[@name='band']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//option[text()='B6H']").click()
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("mark@hashedin")
        self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']").send_keys("12345667890")
        self.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("Mumbai")


x = AddEmployee()
x.employee()
