# ！/usr/bin/python
#author:xx


import xlrd
from utils.public import *
from utils.excel_col import *
from xlutils.copy import copy

class OperationExcel():
	def getExcel(self):
		work=xlrd.open_workbook(data_dir('data','data.xls'))
		sheet=work.sheet_by_index(0)
		return sheet

	def getRows(self):
		return self.getExcel().nrows

	def get_cell_value(self,row,col):
		return self.getExcel().cell_value(row,col)

	def getCaseid(self,row):
		return self.get_cell_value(row,get_Caseidcol())

	def getUrl(self,row):
		return self.get_cell_value(row,get_urlcol())

	def getData(self,row):
		return self.get_cell_value(row,get_datacol())

	def getExpect(self,row):
		return self.get_cell_value(row,get_expectcol())

	def getResult(self,row):
		return self.get_cell_value(row,get_resultcol())

	def writeResult(self,row,content):
		'''将测试结果写入Excel 中'''
		col=get_resultcol()
		work=xlrd.open_workbook(data_dir('data','data.xls'))
		old=copy(work)
		sheet=old.get_sheet(0)
		sheet.write(row,col,content)
		old.save(data_dir('data','data.xls'))


	def success_case(self):
		count=0
		for i in range(1,self.getRows()):
			if self.getResult(i) == 'pass':
				count=count+1
		return count

	def fail_case(self):
		count=0
		for i in range(1,self.getRows()):
			if self.getResult(i) == 'fail':
				count=count+1
		return count

	def success_rate(self):
		rate=''
		if self.fail_case()==0:
			rate='100%'
		else:
			rate=str((self.success_case()/self.fail_case()))+'%'
		return rate









