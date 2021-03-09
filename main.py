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
from mod import TestAutomation

class PosType(unittest.TestCase):
    
    url = 'https://about.postype.com/'
    version = '0.0.1'
    
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

    def test_search_field(self):

        wait = WebDriverWait(self.driver, 20)
        self.driver.get(self.url)
        test = TestAutomation(self.driver)

        test.clickBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 보기')

        test.checkText('//div[@id="navbar-collapse"]/ul/li[1]/a', '포스타입 소개')
        test.checkText('//div[@id="navbar-collapse"]/ul/li[2]/a', '채용 정보')
        test.checkText('//div[@id="navbar-collapse"]/ul/li[3]/a', '블로그')
        test.checkText('//div[@id="navbar-collapse"]/ul/li[4]/a', '비즈니스')

    # def tearDown(self):
        # self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PosType)
    unittest.TextTestRunner(verbosity=2).run(suite)