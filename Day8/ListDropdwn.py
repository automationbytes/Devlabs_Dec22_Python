from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.redbus.in/")
driver.implicitly_wait(30)

driver.find_element(By.XPATH,'//input[@id="src"]').send_keys("Kol")
fromdrop = driver.find_elements(By.XPATH,'//ul[@class="autoFill homeSearch"]/li')

for f in fromdrop:
    print(f.text)
    if "Airport" in f.text:
        f.click()
        break

driver.find_element(By.ID,"onward_cal").click()

for i in range(12):
    monthtitle = driver.find_element(By.XPATH,'//td[@class="monthTitle"]').text
    if "Jun" in monthtitle:
        date = driver.find_elements(By.XPATH, '//table[@class="rb-monthTable first last"]//td')
        for d in date:
            print(d.text)
            if d.text == "19":
                d.click()
                break

    else:
        driver.find_element(By.XPATH,'//td[@class="next"]/button').click()



