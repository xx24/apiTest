# ！/usr/bin/python
#author:xx


import unittest
from utils.operationExcel import *
from email.mime.text import MIMEText
import smtplib

class Runner:
	def __init__(self):
		self.excel=OperationExcel()

	def getSuit(self):
		suit=unittest.TestLoader().discover(
			start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),'tests'),
			pattern='test_*.py',
			top_level_dir=None
		)
		return suit

	def send_mail(self, to_user, sub, content):
		'''
		发送邮件内容
		:param to_user:发送邮件的人
		:param sub:主题
		:param content:邮件内容
		'''
		global send_mail
		global send_user
		send_mail = 'smtp.163.com'
		send_user = '15167195737@163.com'
		message = MIMEText(content, _subtype='plain', _charset='utf-8')
		message['Subject'] = sub+'11'
		message['From'] = send_user
		message['To'] = to_user
		server = smtplib.SMTP()
		server.connect(host=send_mail,port=25)
		server.login('15167195737@163.com', 'xx675737')
		server.sendmail(send_user, to_user, message.as_string())
		server.close()


	def main_run(self):
		unittest.TextTestRunner().run(self.getSuit())
		content='成功用例数：{0} , 失败用例数：{1} , 测试用例成功率：{2}'.format(
			self.excel.success_case(),self.excel.fail_case(),self.excel.success_rate())
		print('sending.....')
		self.send_mail('15167195737@163.com','自动化测试报告',content)



if __name__ == '__main__':
    Runner().main_run()

