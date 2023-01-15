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

driver.get("https://emicalculator.net/")
driver.implicitly_wait(30)

act = ActionChains(driver)
# act.click_and_hold(driver.find_element(By.XPATH,"//span[text()='50L']/parent::span"))
# act.release(driver.find_element(By.XPATH,"//span[text()='125L']/parent::span"))
# act.perform()


act.drag_and_drop(driver.find_element(By.XPATH,"//span[text()='50L']/parent::span"),driver.find_element(By.XPATH,"//span[text()='150L']/parent::span"))
act.perform()
time.sleep(5)
#sep action
# act.scroll_to_element(driver.find_element(By.ID,"startmonthyear"))
# act.perform()

driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element(By.ID,"startmonthyear"))