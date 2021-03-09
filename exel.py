import os
import openpyxl
 
class Exel():

	def __init__(self, num):
		self.num = num
		self.currentPath = os.getcwd()

		self.write_wb = openpyxl.load_workbook(self.currentPath + '/TC.xlsx')
		self.write_ws = self.write_wb.active
	
	def loadSubject(self):
		print('%d. ' %self.num + self.write_ws.cell(row=1+self.num,column=2).value)

	def writeResult(self, result):
		self.write_ws.cell(row=1+self.num,column=6).value = result
		self.write_wb.save(self.currentPath + '/TC.xlsx')