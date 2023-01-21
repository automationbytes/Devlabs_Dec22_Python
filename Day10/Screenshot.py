from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
import time
import datetime
import calendar


driver.get("https://redbus.in")
print(datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S"))
gmt  = time.gmtime()
print(calendar.timegm(gmt))
t = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
driver.get_screenshot_as_file("screenst_"+str(t)+".png")
driver.get_full_page_screenshot_as_file("fullscr.png")

driver.get_screenshot_as_png()