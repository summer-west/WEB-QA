from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time

class TestAutomation():

	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 20)

	def clickBtn(self, xpath, ref):
		try:
			el = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
			el.click()
			print('Passed - ' + ref)
		except TimeoutException:
			print('Failed - TimeoutException')

	def backBtn(self, ref):
		self.driver.back()
		print('Passed - 뒤로가기 (' + ref + ')')

	def checkURL(self, ref):
		url = self.driver.current_url()
		print(url)
		# if url == ref:
		# 	print('Passed - 화면 이동 (' + ref + ')')
		# else:
		# 	print('Failed - 화면 이동 (' + ref + ')')

	def checkText(self, xpath, ref):
		try:
			el = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
			if el.text == ref:
				print ('Passed - ' + ref)
			else:
				print ('Failed - ' + el.text)
		except TimeoutException:
			print('Failed - TimeoutException')


