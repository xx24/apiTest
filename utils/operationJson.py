# ！/usr/bin/python
#author:xx

import json
from utils.public import *
from utils.operationExcel import *

class OperationJson():
	def __init__(self):
		self.excel=OperationExcel()

	def getReadJson(self):
		with open(data_dir('data','data_json.json')) as f:
			data=json.load(f)
			return data

	def getJsonData(self,row):
		return json.dumps(self.getReadJson()[self.excel.getData(row)])



