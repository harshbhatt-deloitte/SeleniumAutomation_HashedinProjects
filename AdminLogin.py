from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    def __init__(self):
        self.url = "https://hashedin-frontend-urtjok3rza-wl.a.run.app/"
        self.id = "admin"
        self.pss = "admin"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value="//input[@id='username']").send_keys(self.id)
        self.driver.find_element(by=By.XPATH, value="//input[@id='password']").send_keys(self.pss)
        self.driver.find_element(by=By.XPATH, value="//input[@id='login']").click()


#x = Login()
