import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class AddEmployee(unittest.TestCase):

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
        self.driver.implicitly_wait(5)
        # a = ActionChains(self.driver)
        # m = self.driver.find_element(By.XPATH, "//a[@href='/admin/add-profile']").click()
        # a.move_to_element(m).perform()

        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-profile']").is_enabled()
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-profile']").is_displayed()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-profile']").click()
        self.driver.implicitly_wait(5)

        assert self.driver.find_element(By.XPATH, "//input[@name='name']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Mark")

        assert self.driver.find_element(By.XPATH, "//input[@name='username']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("mark101")

        assert self.driver.find_element(By.XPATH, "//input[@name='password']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("qwerty")

        assert self.driver.find_element(By.XPATH, "//select[@name='roles']").is_displayed()
        self.driver.find_element(By.XPATH, "//select[@name='roles']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, "//option[@value='user']").click()
        self.driver.implicitly_wait(3)

        assert self.driver.find_element(By.XPATH, "//input[@name='skills_input']").is_displayed()

        self.driver.find_element(By.XPATH, "//input[@name='skills_input']").click()
        skills = self.driver.find_elements(By.XPATH, "//ul[@class='optionContainer']/li")
        for i in skills:
            if i.text == "Java13":
                i.click()

        self.driver.implicitly_wait(3)

        # assert self.driver.find_elements(By.XPATH, "//option[text()='Select Specialization']")
        self.driver.find_element(By.XPATH, "//option[text()='Backend']").click()

        assert self.driver.find_element(By.XPATH, "//select[@name='band']").is_displayed()
        self.driver.find_element(By.XPATH, "//select[@name='band']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, "//option[text()='B7H']").click()

        assert self.driver.find_element(By.XPATH, "//input[@name='email']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("mark@hashedin")

        assert self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']").send_keys("12345667890")

        assert self.driver.find_element(By.XPATH, "//input[@name='address']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("Mumbai")

        assert self.driver.find_element(By.XPATH, "//button[text()='Add Profile']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//button[text()='Add Profile']").is_enabled()
        self.driver.find_element(By.XPATH, "//button[text()='Add Profile']").click()
        assert self.driver.find_element(By.XPATH, "// div[text() = 'Added successfully']").is_displayed()
        assert self.driver.find_element(By.XPATH, "// button[text() = 'OK']").click()
        time.sleep(5)
