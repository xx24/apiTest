# ！/usr/bin/python
#author:xx

import requests
from utils.operationJson import *
from utils.operationExcel import *

class Method():
	def __init__(self):
		self.excel=OperationExcel()
		self.json=OperationJson()

	def postMethod(self,row,data):
		try:
			result = requests.post(
				url=self.excel.getUrl(row),
				headers=getHeaders(),
				data=data,
				timeout=6
			)
			return result
		except Exception as e:
			print('post请求失败')


	def getMethod(self,row,params=None):
		try:
			result = requests.get(
				url=self.excel.getUrl(row),
				params=params,
				headers=getHeaders(),
				timeout=6
			)
			return result
		except Exception as e:
			print('get请求失败')

class IsAssert():
	def __init__(self):
		self.opexcel=OperationExcel()

	def isContent(self,row,str2):
		flag=None
		if self.opexcel.getExpect(row)==str2:
			flag=True
		else:
			flag=False
		return flag
