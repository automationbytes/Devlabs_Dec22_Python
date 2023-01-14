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
'''
Select dropdown

3 ways

1)Selectbyvalue - value attribute in option tag
2)Selectbyvisibletext - based on value available in UI
3)Selectbyindex - based on order of occurance

'''

country =  Select(driver.find_element(By.XPATH,'//select[@id="BillingCountryId"]'))
#country.select_by_value("88")
#country.select_by_visible_text("Australia")
#country.select_by_index(3)

for c in country.options:
    print(c.text)
    if c.text == "Yemen":
        c.click()
        break