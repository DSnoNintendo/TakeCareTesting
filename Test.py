import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep

class Browser:
    def __init__(self):
        self.browserOpen = False
        self.driver = None
        self.timeout = None
        self.max = None
        self.counter = 0
        self.start = None

        try:
            # try to open ChromeDriver
            browser_options = ChromeOptions()
            #browser_options.headless = True
            browser_options.add_argument('--disable-dev-shm-usage')
            browser_options.add_argument('--no-sandbox')
            # if webdriver not installed, install it
            #version 2.26 is a stable version for testing
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
            self.browserOpen = True
        except ValueError:  # if chrome not available, try firefox
            # try to open FirefoxDriver
            browser_options = FirefoxOptions()
            #browser_options.headless = True
            browser_options.add_argument('--disable-dev-shm-usage')
            browser_options.add_argument('--no-sandbox')
            # if firefox driver not installed, install it
            self.driver = webdriver.Firefox(GeckoDriverManager().install(), options=browser_options)
            self.browserOpen = True
        except:
            self.browserOpen = False


    def acceptAlert(self):
        self.driver.switch_to.alert.accept()

    def getAlertText(self):
        return self.driver.switch_to.alert.text

    def browserIsOpen(self):
        return self.browserOpen

    def click(self, xpath):
        sleep(0.4)
        self.driver.find_element(by=By.XPATH, value=xpath).click()


    def input(self, xpath, characters):
        self.driver.find_element(by=By.XPATH, value=xpath).send_keys(characters)

    def goTo(self, destination):
        self.driver.get(destination)
