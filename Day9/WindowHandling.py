'''

windowhandle - current window
windowhandles - all open windows

'''
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.irctc.co.in/nget/train-search")
driver.implicitly_wait(30)

time.sleep(5)
wait = WebDriverWait(driver,20)
wait.until(expected_conditions.element_to_be_clickable(driver.find_element(By.XPATH,"//button[text()='Later']")))
driver.find_element(By.XPATH,"//button[text()='Later']").click()

driver.find_element(By.XPATH,"//a[text()=' BUSES ']").click()
driver.find_element(By.XPATH,"//a[text()=' FLIGHTS ']").click()
driver.find_element(By.XPATH,"//a[text()=' HOTELS ']").click()

print(driver.current_url)

parentwindow = driver.current_window_handle
print(parentwindow)

allopenwindows = driver.window_handles #4 #include parent wndow also
print(allopenwindows)
print(len(allopenwindows))
print(type(allopenwindows)) #list

time.sleep(3)
for a in allopenwindows:
    if a != parentwindow:

        driver.switch_to.window(a)
        print(driver.current_url)

        if "hotel" in driver.current_url:
            driver.find_element(By.ID,"filterText").send_keys("Taj")
        else:
            driver.close()


driver.switch_to.window(parentwindow)
print(driver.current_url)
