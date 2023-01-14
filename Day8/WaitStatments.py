'''
implicitwait - it iwll b available for all elements
explicit wait - for particular element, add a condition to it

'''

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(30)

driver.find_element(By.ID,"user-name").send_keys("performance_glitch_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

wait = WebDriverWait(driver,15)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//img[@alt="Sauce Labs Backpack"]')))
driver.find_element(By.XPATH,'//img[@alt="Sauce Labs Backpack"]').click()


