import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Login(unittest.TestCase):
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

    def test_verify(self):
        self.driver.implicitly_wait(5)
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/managers']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/managers']").is_enabled()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/managers']").click()
        self.driver.implicitly_wait(5)

        found = False
        lst = self.driver.find_elements(By.XPATH, "//div[@class='profile-card']/header/div")
        for i in lst:
            if i.text == "manager":
                found = True
                break
        self.assertTrue(found)

        time.sleep(5)



