from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://admin-demo.nopcommerce.com/Admin/Order/List")

driver.find_element(By.XPATH,'//input[@data-val-email="Wrong email"]').clear()
driver.find_element(By.XPATH,'//input[@data-val-email="Wrong email"]').send_keys("admin@yourstore.com")

driver.find_element(By.XPATH,'//input[@id="Password"]').clear()
driver.find_element(By.XPATH,'//input[@id="Password"]').send_keys("admin")

driver.find_element(By.XPATH,'//input[@id="RememberMe"]').click()
driver.find_element(By.XPATH,"//button[text()='Log in']").click()

driver.find_element(By.XPATH,'//span[@aria-controls="StartDate_dateview"]').click()

day = driver.find_elements(By.XPATH,'//table[@class="k-content k-month"]//a')
for d in day:
    print(d.text)