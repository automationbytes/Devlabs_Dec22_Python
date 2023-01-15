import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.snapdeal.com/")
driver.implicitly_wait(30)


driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH,"//span[text()='Mattresses']"))
time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element(By.NAME,"keyword"))