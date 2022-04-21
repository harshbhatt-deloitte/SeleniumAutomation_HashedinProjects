import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class AddBand(unittest.TestCase):

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

    def test_band(self):
        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-band']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-band']").is_enabled()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-band']").click()

        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "// input[ @ name = 'band']").is_displayed()

        self.driver.find_element(By.XPATH, "// input[ @ name = 'band']").send_keys("B6L")
        assert self.driver.find_element(By.XPATH, "//button[text()='Add Band']").is_enabled()

        self.driver.find_element(By.XPATH, "//button[text()='Add Band']").click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH, "//div[text()='Band Added']").is_displayed()
        self.driver.find_element(By.XPATH, "//button[text()='OK']").click()
        time.sleep(10)

    # Negative test case for adding the same band again
    def test_Re_band(self):
        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-band']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-band']").is_enabled()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-band']").click()

        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "// input[ @ name = 'band']").is_displayed()

        self.driver.find_element(By.XPATH, "// input[ @ name = 'band']").send_keys("B99")
        assert self.driver.find_element(By.XPATH, "//button[text()='Add Band']").is_enabled()

        self.driver.find_element(By.XPATH, "//button[text()='Add Band']").click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH, "//div[@class='swal-text']").is_displayed()
        self.driver.find_element(By.XPATH, "//button[text()='OK']").click()
        time.sleep(10)

    def test_DeleteBand(self):
        # assert self.driver.find_element(By.XPATH, "").is_displayed()
        # //*[@id="root"]/div/div/div[2]/div[2]/div/div/table/tbody/tr[4]/td[3]/span
        time.sleep(5)
        # assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-band']").is_displayed()
        # assert self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-band']").is_enabled()
        self.driver.find_element(By.XPATH, "//a[@href='/admin/add-new-band']").click()
        time.sleep(5)

        lstEle = self.driver.find_elements(By.XPATH, "//tbody/tr/td[2]")
        lstDel = self.driver.find_elements(By.XPATH, "//tbody/tr/td[3]/span")

        found = 0
        for i in range(0, len(lstEle)):
            if lstEle[i].text == "B10":
                lstDel[i].click()

        time.sleep(5)

