from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
import time

class TestAutomation():

	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 20)

	def setURL(self, url):
		self.driver.get(url)

	def checkBtn(self, xpath, ref):
		try:
			self.driver.switch_to.window(self.driver.window_handles[-1])
			self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
			print('Passed - ' + ref)
		except TimeoutException:
			print('Failed - TimeoutException')

	def clickBtn(self, xpath, ref):
		try:
			el = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
			el.click()
			print('Passed - ' + ref)
			return True
		except TimeoutException:
			print('Failed - TimeoutException')
			return False

	def backBtn(self):
		self.driver.back()
		print('Passed - 뒤로가기')

	def checkURL(self, ref):
		self.driver.switch_to.window(self.driver.window_handles[-1])
		url = self.driver.current_url
		if url in ref:
			print('Passed - 접속 URL (' + ref + ')')
		else:
			print('Failed - 접속 URL (' + ref + ')')

	def checkText(self, xpath, ref):
		try:
			self.driver.switch_to.window(self.driver.window_handles[-1])
			el = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
			if el.text == ref:
				print ('Passed - ' + ref)
			else:
				print ('Failed - ' + el.text)
		except TimeoutException:
			print('Failed - TimeoutException')

	def checkUI(self, xpath, ref):
		try:
			self.driver.switch_to.window(self.driver.window_handles[-1])
			self.driver.find_element_by_xpath(xpath)
			print('Passed - ' + ref)
		except WebDriverException:
			print('Failed - WebDriverException')
		except NoSuchWindowException:
			print('Failed - NoSuchWindowException')			

