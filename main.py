import unittest
import os
import subprocess
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from index import Index

class PosType(unittest.TestCase):
    
    version = '0.0.2'
    
    def printVersion(self):
        print('version : ' + self.version)
        

    def setUp(self):
        self.printVersion()
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
              'platformName': 'Android',
              'browserName': 'Chrome'
            })
        self.index = Index(self.driver)

    def test_search_field(self):

        for num in range(1, 19):
            self.index.runTestCase(num)
        
    # def tearDown(self):
        # self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PosType)
    unittest.TextTestRunner(verbosity=2).run(suite)
