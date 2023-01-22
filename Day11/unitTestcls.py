import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import unittest

class LaunchURL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    def test_google(self):
        self.driver.get("https://www.google.com/")
        self.driver.get_screenshot_as_file("google.png")
        print(self.driver.current_url)
        print(self.driver.title)

    def test_yahoo(self):
        self.driver.get("https://www.yahoo.com/")
        self.driver.get_screenshot_as_file("yahoo.png")
        print(self.driver.current_url)
        print(self.driver.title)

    def test_bing(self):
        self.driver.get("https://www.bing.com/")
        self.driver.get_screenshot_as_file("bing.png")
        print(self.driver.current_url)
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()
