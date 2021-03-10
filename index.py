import unittest
import os
import subprocess
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
import time
from mod import TestAutomation
from exel import Exel

class Index():

    url = 'https://about.postype.com/'
    
    def __init__(self, driver):
        self.ex = Exel()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.test = TestAutomation(self.driver)

    def runTestCase(self, num):

        result = True
        self.ex.loadSubject(num)

        if num == 1:
            self.test.setURL(self.url)
            result = self.test.checkURL('https://about.postype.com/')

        elif num == 2:
            result = self.test.checkBtn('/html/body/nav/div/a', 'POSTYPE 로고 표시')
            result = self.test.clickBtn('/html/body/nav/div/a', 'POSTYPE 로고 클릭') and result
            result = self.test.checkURL('https://about.postype.com/index') and result

        elif num == 3:
            result = self.test.checkBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 표시')
            result = self.test.clickBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 클릭') and result

        elif num == 4:
            result = self.test.checkText('//div[@id="navbar-collapse"]/ul/li[1]/a', '포스타입 소개')
            result = self.test.checkText('//div[@id="navbar-collapse"]/ul/li[2]/a', '채용 정보') and result
            result = self.test.checkText('//div[@id="navbar-collapse"]/ul/li[3]/a', '블로그') and result
            result = self.test.checkText('//div[@id="navbar-collapse"]/ul/li[4]/a', '비즈니스') and result

        elif num == 5:
            result = self.test.clickBtn('//div[@id="navbar-collapse"]/ul/li[1]/a', '[포스타입 소개]')
            result = self.test.checkURL('https://about.postype.com/index') and result

        elif num == 6:
            result = self.test.clickBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 클릭')
            result = self.test.clickBtn('//div[@id="navbar-collapse"]/ul/li[2]/a', '[채용 정보]') and result
            result = self.test.checkURL('https://about.postype.com/jobs') and result

        elif num == 7:
            result = self.test.clickBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 클릭')
            result = self.test.clickBtn('//div[@id="navbar-collapse"]/ul/li[3]/a', '[블로그]') and result
            result = self.test.checkURL('https://about.postype.com/blog') and result

        elif num == 8:
            result = self.test.clickBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 클릭')
            result = self.test.clickBtn('//div[@id="navbar-collapse"]/ul/li[4]/a', '[비즈니스]') and result
            result = self.test.checkURL('https://about.postype.com/business') and result
            self.test.setURL(self.url)

        elif num == 9:
            result = self.test.checkUI('/html/body/main/div/section[3]/div[2]/article[1]/a', '언론기사(1) UI 표시')
            result = self.test.checkUI('/html/body/main/div/section[3]/div[2]/article[2]/a', '언론기사(2) UI 표시') and result
            result = self.test.checkUI('/html/body/main/div/section[3]/div[2]/article[3]/a', '언론기사(3) UI 표시') and result
            self.test.setURL(self.url)

        elif num == 10:
            result = self.test.checkBtn('/html/body/main/section[2]/div/div/a', '채용 정보 살펴보기 버튼 표시')
            result = self.test.clickBtn('/html/body/main/section[2]/div/div/a', '채용 정보 살펴보기 버튼 클릭') and result
            result = self.test.checkURL('https://about.postype.com/jobs') and result
            self.test.setURL(self.url)

        elif num == 11:
            result = self.test.checkText('/html/body/footer/div/ul/li[1]/a', '웹서비스')
            result = self.test.checkText('/html/body/footer/div/ul/li[2]/a', 'Android') and result
            result = self.test.checkText('/html/body/footer/div/ul/li[3]/a', 'iOS') and result
            result = self.test.checkText('/html/body/footer/div/ul/li[4]/a', '공식 블로그') and result
            result = self.test.checkText('/html/body/footer/div/ul/li[5]/a', '팀 블로그') and result
            result = self.test.checkText('/html/body/footer/div/ul/li[2]/a', 'Android') and result
            result = self.test.checkText('/html/body/footer/div/ul/li[6]/a', '공식 Instagram') and result
            result = self.test.checkText('/html/body/footer/div/ul/li[7]/a', '팀 Instagram') and result

        elif num == 12:
            result = self.test.checkText('/html/body/footer/div/ul/li[1]/a', '웹서비스')
            result = self.test.clickBtn('/html/body/footer/div/ul/li[1]/a', '[웹서비스]') and result
            result = self.test.checkURL('https://www.postype.com/') and result
            self.test.setURL(self.url)      

        elif num == 13:
            result = self.test.checkText('/html/body/footer/div/ul/li[2]/a', 'Android')
            result = self.test.clickBtn('/html/body/footer/div/ul/li[2]/a', '[Android]') and result
            result = self.test.checkURL('https://play.google.com/store/apps/details?id=com.postype.play') and result
            self.test.setURL(self.url)      

        elif num == 14:
            result = self.test.checkText('/html/body/footer/div/ul/li[3]/a', 'iOS') and result
            result = self.test.clickBtn('/html/body/footer/div/ul/li[3]/a', '[iOS]') and result
            result = self.test.checkURL('https://apps.apple.com/kr/app/%ED%8F%AC%EC%8A%A4%ED%83%80%EC%9E%85-postype-%EC%B0%BD%EC%9E%91-%EC%BD%98%ED%85%90%EC%B8%A0-%EC%98%A4%ED%94%88-%ED%94%8C%EB%9E%AB%ED%8F%BC/id1502367642') and result
            self.test.setURL(self.url)         

        elif num == 15:
            result = self.test.checkText('/html/body/footer/div/ul/li[4]/a', '공식 블로그') and result
            result = self.test.clickBtn('/html/body/footer/div/ul/li[4]/a', '[공식 블로그]') and result
            result = self.test.checkURL('https://blog.postype.com/') and result
            self.test.setURL(self.url)      

        elif num == 16:
            result = self.test.checkText('/html/body/footer/div/ul/li[5]/a', '팀 블로그') and result
            result = self.test.clickBtn('/html/body/footer/div/ul/li[5]/a', '[팀 블로그]') and result
            result = self.test.checkURL('https://team.postype.com/') and result
            self.test.setURL(self.url)      

        elif num == 17:
            result = self.test.checkText('/html/body/footer/div/ul/li[6]/a', '공식 Instagram') and result
            result = self.test.clickBtn('/html/body/footer/div/ul/li[6]/a', '[공식 Instagram]') and result
            result = self.test.checkURL('https://www.instagram.com/postype_official/') and result
            self.test.setURL(self.url)      

        elif num == 18:
            result = self.test.checkText('/html/body/footer/div/ul/li[7]/a', '팀 Instagram') and result
            result = self.test.clickBtn('/html/body/footer/div/ul/li[7]/a', '[팀 Instagram]') and result
            result = self.test.checkURL('https://www.instagram.com/postype_team/') and result
            self.test.setURL(self.url)
        else:
            print('\n- Test 종료 -')      

        self.ex.writeResult(num, result)
    
