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
form elsel import Exel

class Index():

    url = ''
    
    def __init__(self):
        self.ex = Exel()
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
              'platformName': 'Android',
              'browserName': 'Chrome'
            })

        self.wait = WebDriverWait(self.driver, 20)
        self.url = 'https://about.postype.com/'
        

    def runTestCase(self):

        self.driver.get(self.url)
        test = TestAutomation(self.driver)
        
        print('\n01 POSTYPE 채용안내 페이지 접속')
        test.checkURL('https://about.postype.com/')

        print('\n02 POSTYPE 로고 확인')
        test.checkBtn('/html/body/nav/div/a', 'POSTYPE 로고 표시')
        test.checkBtn('/html/body/nav/div/a', 'POSTYPE 로고 클릭')
        test.checkURL('https://about.postype.com/')        

        print('\n03 네비게이션 버튼 확인')
        test.checkBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 표시')      
        test.clickBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 클릭')

        print('\n04 네비게이션 메뉴 확인')    
        test.checkText('//div[@id="navbar-collapse"]/ul/li[1]/a', '포스타입 소개')
        test.checkText('//div[@id="navbar-collapse"]/ul/li[2]/a', '채용 정보')
        test.checkText('//div[@id="navbar-collapse"]/ul/li[3]/a', '블로그')
        test.checkText('//div[@id="navbar-collapse"]/ul/li[4]/a', '비즈니스')

        print('\n05 네비게이션 - [포스타입 소개] 메뉴 동작 확인')
        test.clickBtn('//div[@id="navbar-collapse"]/ul/li[1]/a', '[포스타입 소개]')
        test.checkURL('https://about.postype.com/index')

        print('\n06 네비게이션 - [채용 정보] 메뉴 동작 확인')
        test.clickBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 클릭')
        test.clickBtn('//div[@id="navbar-collapse"]/ul/li[2]/a', '[채용 정보]')
        test.checkURL('https://about.postype.com/jobs')

        print('\n07 네비게이션 - [블로그] 메뉴 동작 확인')
        test.clickBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 클릭')        
        test.clickBtn('//div[@id="navbar-collapse"]/ul/li[3]/a', '[블로그]')
        test.checkURL('https://about.postype.com/blog')

        print('\n08 네비게이션 - [비즈니스] 메뉴 동작 확인')
        test.clickBtn('//button[@id="navbar-toggler"]', '네비게이션 메뉴 버튼 클릭')       
        test.clickBtn('//div[@id="navbar-collapse"]/ul/li[4]/a', '[비즈니스]')
        test.checkURL('https://about.postype.com/business')
        
        test.backBtn()

        print('\n09 "미디어에서 본 포스타입" 언론기사 UI 확인')
        test.checkUI('/html/body/main/div/section[3]/div[2]/article[1]/a', '언론기사(1) UI 표시')      
        test.checkUI('/html/body/main/div/section[3]/div[2]/article[2]/a', '언론기사(2) UI 표시')
        test.checkUI('/html/body/main/div/section[3]/div[2]/article[3]/a', '언론기사(3) UI 표시')  

        print('\n10 [채용정보 살펴보기] 버튼 확인')
        test.checkBtn('/html/body/main/section[2]/div/div/a', '채용 정보 살펴보기 버튼 표시')
        test.clickBtn('/html/body/main/section[2]/div/div/a', '채용 정보 살펴보기 버튼 클릭')
        test.checkURL('https://about.postype.com/jobs')
        test.backBtn()

        print('\n11 하단 바로가기 메뉴 확인')
        test.checkText('/html/body/footer/div/ul/li[1]/a', '웹서비스')
        test.checkText('/html/body/footer/div/ul/li[2]/a', 'Android')
        test.checkText('/html/body/footer/div/ul/li[3]/a', 'iOS')
        test.checkText('/html/body/footer/div/ul/li[4]/a', '공식 블로그')
        test.checkText('/html/body/footer/div/ul/li[5]/a', '팀 블로그')
        test.checkText('/html/body/footer/div/ul/li[6]/a', '공식 Instagram')
        test.checkText('/html/body/footer/div/ul/li[7]/a', '팀 Instagram')
        
        print('\n12 하단 바로가기 - [웹서비스] 메뉴 동작 확인')
        test.checkText('/html/body/footer/div/ul/li[1]/a', '웹서비스')
        test.clickBtn('/html/body/footer/div/ul/li[1]/a', '[웹서비스]')
        test.checkURL('https://www.postype.com/')
        test.setURL(self.url)

        print('\n13 하단 바로가기 - [Android] 메뉴 동작 확인')
        test.checkText('/html/body/footer/div/ul/li[2]/a', 'Android')
        test.clickBtn('/html/body/footer/div/ul/li[2]/a', '[Android]')
        test.checkURL('https://play.google.com/store/apps/details?id=com.postype.play')
        test.setURL(self.url)

        print('\n14 하단 바로가기 - [iOS] 메뉴 동작 확인')
        test.checkText('/html/body/footer/div/ul/li[3]/a', 'iOS')
        test.clickBtn('/html/body/footer/div/ul/li[3]/a', '[iOS]')        
        test.checkURL('https://apps.apple.com/kr/app/%ED%8F%AC%EC%8A%A4%ED%83%80%EC%9E%85-postype-%EC%B0%BD%EC%9E%91-%EC%BD%98%ED%85%90%EC%B8%A0-%EC%98%A4%ED%94%88-%ED%94%8C%EB%9E%AB%ED%8F%BC/id1502367642')
        test.setURL(self.url)

        print('\n15 하단 바로가기 - [공식 블로그] 메뉴 동작 확인')
        test.checkText('/html/body/footer/div/ul/li[4]/a', '공식 블로그')
        test.clickBtn('/html/body/footer/div/ul/li[4]/a', '[공식 블로그]')       
        test.checkURL('https://blog.postype.com/')
        test.setURL(self.url)

        print('\n16 하단 바로가기 - [팀 블로그] 메뉴 동작 확인')
        test.checkText('/html/body/footer/div/ul/li[5]/a', '팀 블로그')
        test.clickBtn('/html/body/footer/div/ul/li[5]/a', '[팀 블로그]')        
        test.checkURL('https://team.postype.com/')
        test.setURL(self.url)        

        print('\n17 하단 바로가기 - [공식 Instagram] 메뉴 동작 확인')
        test.checkText('/html/body/footer/div/ul/li[6]/a', '공식 Instagram')
        test.clickBtn('/html/body/footer/div/ul/li[6]/a', '[공식 Instagram]')      
        test.checkURL('https://www.instagram.com/postype_official')
        test.setURL(self.url)      

        print('\n18 하단 바로가기 - [팀 Instagram] 메뉴 동작 확인')
        test.checkText('/html/body/footer/div/ul/li[6]/a', '공식 Instagram')
        test.clickBtn('/html/body/footer/div/ul/li[6]/a', '[팀 Instagram]')       
        test.checkURL('https://www.instagram.com/postype_team')
        test.setURL(self.url)



if __name__ == '__main__':
    Summer = Index()
    Summer.runTestCase()