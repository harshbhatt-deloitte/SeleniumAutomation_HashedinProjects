import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class AddSpec(unittest.TestCase):

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

    def test_AddSpec(self):
        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-designation']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-designation']").is_enabled()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-designation']").click()
        time.sleep(5)

        assert self.driver.find_element(By.XPATH, "// input[ @ name = 'designation']").is_displayed()
        self.driver.find_element(By.XPATH, "// input[ @ name = 'designation']").send_keys("QA")
        self.driver.find_element(By.XPATH, "//button[text() = 'Add Specialization']").click()
        time.sleep(3)

        assert self.driver.find_element(By.XPATH, "//div[text()='Specialization Added Succesfully']").is_displayed()
        self.driver.find_element(By.XPATH, "//button[text() = 'OK']").click()
        time.sleep(5)

    # Negative Test case for adding the same specialization again
    def test_Re_Spec(self):
        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-designation']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-designation']").is_enabled()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-designation']").click()
        time.sleep(5)

        assert self.driver.find_element(By.XPATH, "// input[ @ name = 'designation']").is_displayed()
        self.driver.find_element(By.XPATH, "// input[ @ name = 'designation']").send_keys("QA")
        self.driver.find_element(By.XPATH, "//button[text() = 'Add Specialization']").click()
        time.sleep(3)

        assert self.driver.find_element(By.XPATH, "//div[@class='swal-text']").is_displayed()
        self.driver.find_element(By.XPATH, "//button[text() = 'OK']").click()
        time.sleep(5)




