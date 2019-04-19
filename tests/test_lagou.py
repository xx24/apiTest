# ！/usr/bin/python
#author:xx

import unittest
from base.method import *
from utils.operationExcel import *
from utils.operationJson import *
from page.lagouData import *


class Test_Lagou(unittest.TestCase):
	def setUp(self) -> None:
		self.method=Method()
		self.isAssert=IsAssert()
		self.excel=OperationExcel()
		self.json=OperationJson()

	def test_001(self,row=1):
		'''检查期望值与实际值是否相等'''
		r=self.method.postMethod(row,self.json.getJsonData(row))
		if self.isAssert.isContent(row,r.json()['state']):
			self.excel.writeResult(row, 'pass')
		else:
			self.excel.writeResult(row, 'fail')

	def test_002(self,row=1):
		'''动态参数请求'''
		r=self.method.postMethod(row,setkd(row,'python工程师'))
		list1=[]
		for i in range(15):
			positionid=r.json()['content']['positionResult']['result'][i]['positionId']
			list1.append(positionid)
		writePositionId(json.dumps(list1))

if __name__ == '__main__':
    unittest.main(verbosity=2)







