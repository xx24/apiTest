# ！/usr/bin/python
#author:xx

from utils.operationJson import *
import json

op=OperationJson()

def setkd(row,kd):
	'''将请求data中的kd赋值'''
	dict1=json.loads(op.getJsonData(row))
	dict1['kd']=kd
	return json.dumps(dict1)

def writePositionId(content):
	'''将数据存到positionId文件中'''
	with open(data_dir('data','position'),'w') as f:
		f.write(content)

def getPositionId():
	'''读取文件，返回list类型数据'''
	with open(data_dir('data','position'),'r') as f:
		return json.loads(f.read())

def getInfo():
	'''得倒不同的url，并返回存放所有url的list'''
	list1=[]
	for item in getPositionId():
		url='https://www.lagou.com/jobs/{0}.html'.format(item)
		list1.append(url)
	return list1
