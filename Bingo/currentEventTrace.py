import json
import urllib2
import requests
import datetime 
import time 
while True:
	url = 'http://test-bng-sec01.giocodigitale.sps/b4m-fe/gaming/currentEvent'
	data = '''{"roomCode": "03"}'''
        requestTime = str(datetime.datetime.now())
	response = requests.post(url, data=data,headers={"Content-Type": "application/json"})
	##print "code:"+ str(response.status_code)
	##print "******************"
	##print "headers:"+ str(response.headers)
	##.print "******************"
	responseTime = str(datetime.datetime.now())
	print "requestTime:"+requestTime+","+ "responseTime:"+ responseTime + ","+ str(response.text)
	time.sleep(6)
