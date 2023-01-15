'''

Switchto

frames - html inside a html
<iframe> -
<frameset> - very very old website. before html4-

3 ways
------
1)id/name
2)index
3)8 locators


alerts
======

4 actions
--------
1) sendkeys
2) text
3) accept
4) dismiss


window handling

'''

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.implicitly_wait(30)

driver.find_element(By.XPATH,'//a[@onclick="retheme()"]').click()
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH,"//button[text()='Try it']").click()

print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys("Devops")
#driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()

#driver.switch_to.parent_frame()

driver.switch_to.default_content()

driver.find_element(By.XPATH,'//a[@onclick="retheme()"]').click()
