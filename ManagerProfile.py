import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class AddManager(unittest.TestCase):

    def setUp(self):
        self.url = "https://hashedin-frontend-urtjok3rza-wl.a.run.app/"
        self.id = "admin"
        self.pss = "admin"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(self.id)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(self.pss)
        self.driver.find_element(By.XPATH, "//input[@id='login']").click()

    def test_addProfile(self):
        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-profile']").is_enabled()
        # a = ActionChains(self.driver)
        # m = self.driver.find_element(By.XPATH, "//a[@href='/admin/add-profile']").click()
        # a.move_to_element(m).perform()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-profile']").click()
        time.sleep(10)
        assert self.driver.find_element(By.XPATH, "//input[@name='name']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys("MarkZ")

        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("mark10")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("qwerty")
        self.driver.find_element(By.XPATH, "//select[@name='roles']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//option[@value='mod']").click()
        # self.driver.find_element(By.XPATH, "//input[@name='skills_input']").send_keys("java")
        time.sleep(5)
        # self.driver.find_elements(By.XPATH, "//select[@name='designation']").click()
        self.driver.find_element(By.XPATH, "//option[text()='Backend']").click()
        self.driver.find_element(By.XPATH, "//select[@name='band']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//option[text()='B8L']").click()
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("mark@hashedin")
        self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']").send_keys("1234566789")
        self.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("Mumbai")

