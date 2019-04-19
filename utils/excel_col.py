# ！/usr/bin/python
#author:xx



EXCEL_CASEID=0
EXCEL_URL=1
EXCEL_TITLE=2
EXCEL_DATA=3
EXCEL_EXPECT=4
EXCEL_RESULT=5

'''获取excel中列数'''
def get_Caseidcol():
	return EXCEL_CASEID

def get_urlcol():
	return EXCEL_URL

def get_titlecol():
	return EXCEL_TITLE

def get_datacol():
	return EXCEL_DATA

def get_expectcol():
	return EXCEL_EXPECT

def get_resultcol():
	return EXCEL_RESULT

def getHeaders():
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie':'user_trace_token=20190409192716-1fe5f6ca-9504-4287-bd21-f5c9da143a90; _ga=GA1.2.917802722.1554809237; LGUID=20190409192717-6e499cac-5aba-11e9-a1c1-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a2956ad9dcb-0bb20b4116ecff-366c7e04-1296000-16a2956ad9e1c9%22%2C%22%24device_id%22%3A%2216a2956ad9dcb-0bb20b4116ecff-366c7e04-1296000-16a2956ad9e1c9%22%7D; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=6; index_location_city=%E6%9D%AD%E5%B7%9E; JSESSIONID=ABAAABAAAGGABCBAF783E1D3D531C20D171ABD3364AB3CE; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554809284,1555471665,1555485794,1555560597; X_HTTP_TOKEN=19e4b5015ac2c45f7728565551d9353668cc5e8d96; _gid=GA1.2.1123586289.1555658277; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555658277; LGSID=20190419151757-419903d2-6273-11e9-905c-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20190419151757-41990535-6273-11e9-905c-525400f775ce; TG-TRACK-CODE=index_search; SEARCH_ID=85e62982b7c24a44931e055777e64980',
		'Referer':'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
	}
	return headers
