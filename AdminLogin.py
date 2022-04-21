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

    def test_login(self):
        assert self.driver.title == "Hashedin Pickup"

    def test_username(self):
        assert self.driver.find_element(By.XPATH, "//input[@name='username']").is_displayed()

    def test_pass(self):
        assert self.driver.find_element(By.XPATH, "//input[@id='password']").is_displayed()

    def test_button(self):
        assert self.driver.find_element(By.XPATH, "//input[@id='login']").is_enabled()


if __name__ == "__main__":
    unittest.main()
