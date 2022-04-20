import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class AddTech(unittest.TestCase):

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

    def test_tech(self):
        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-skill']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-skill']").is_enabled()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-skill']").click()
        time.sleep(5)

        assert self.driver.find_element(By.XPATH, "//input[@name='technology']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@name='technology']").send_keys("Python")
        self.driver.find_element(By.XPATH, "//button[text()='Add Skill']").click()
        time.sleep(3)

        assert self.driver.find_element(By.XPATH, "//div[text()='Technology Added']").is_displayed()
        self.driver.find_element(By.XPATH, "//button[text()='OK']").click()
        time.sleep(10)

    # Negative test case for adding the same technology again
    def test_Re_tech(self):
        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-skill']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-skill']").is_enabled()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-skill']").click()
        time.sleep(5)

        assert self.driver.find_element(By.XPATH, "//input[@name='technology']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@name='technology']").send_keys("Python")
        self.driver.find_element(By.XPATH, "//button[text()='Add Skill']").click()
        time.sleep(3)

        assert self.driver.find_element(By.XPATH, "//div[@class='swal-text']").is_displayed()
        self.driver.find_element(By.XPATH, "//button[text()='OK']").click()
        time.sleep(10)

