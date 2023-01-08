'''
8 locating options

id
name
class name -
tag name
link text -> a
partial link text

xpath
css


'''

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://www.facebook.com/")
driver.find_element(By.ID,"email").send_keys("admin")
# driver.find_element(By.NAME,"pass").send_keys("pass46wrd")
# #driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"otten password?").click()
driver.find_element(By.XPATH,"//a[text()='Create New Account']").click()













