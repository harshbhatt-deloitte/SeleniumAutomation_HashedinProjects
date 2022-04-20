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

    def test_login(self):
        self.driver.find_element(by=By.XPATH, value="//input[@id='username']").send_keys(self.id)
        self.driver.find_element(by=By.XPATH, value="//input[@id='password']").send_keys(self.pss)
        self.driver.find_element(by=By.XPATH, value="//input[@id='login']").click()
        # self.driver.title
        assert self.driver.title == "Hashedin Pickup"

    def test_username(self):
        assert self.driver.find_element(By.XPATH, "//input[@name='username']").is_displayed()

    def test_pass(self):
        assert self.driver.find_element(By.XPATH, "//input[@id='password']").is_displayed()

# x = Login()

if __name__ == "__main__":
    unittest.main()
