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

act = ActionChains(driver)
act.move_by_offset(400,300)

act.move_to_element(driver.find_element(By.XPATH,"//span[text()='Home & Kitchen']"))
act.move_to_element(driver.find_element(By.XPATH,"//span[text()='Mattresses']"))
act.click(driver.find_element(By.XPATH,"//span[text()='Mattresses']"))
act.perform()




