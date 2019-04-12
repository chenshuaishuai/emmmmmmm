# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import urllib
import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Cookie
import cookielib
from lxml import etree
import lxml.html
import sys
# Create your views here.


reload(sys)
sys.setdefaultencoding('utf8')
url1 = 'http://218.198.176.112/default6.aspx'	#教务管理url


def index(request):
	return render(request,'cl/index.html')

def data(request):
	userid = request.POST.get('id')
	password = request.POST.get('pa')
	username = str(request.POST.get('na'))
	nameurl = urllib.quote(str(username))
	url2 = 'http://218.198.176.112/xskbcx.aspx?xh='+userid+'&xm='+nameurl+'&gnmkdm=N121603'	#个人课表url
	loginvalue={
		'__VIEWSTATE':'dDwtMTQxNDAwNjgwODt0PDtsPGk8MD47PjtsPHQ8O2w8aTwyMT47aTwyMz47aTwyNT47aTwyNz47PjtsPHQ8cDxsPGlubmVyaHRtbDs+O2w8XDxsaVw+XDxzcGFuIGNsYXNzPSd0eXBlJ1w+XDwvc3Bhblw+XDxhIGhyZWY9J2dnc20uYXNweD9mYnNqPTIwMTctMDUtMTIgMTI6NDQ6MTEmeXhxeD0yMDE4LTA1LTMxJyB0YXJnZXQ9J19ibGFuaycgICBcPjIwMTflubTnoJTnqbbnlJ/ogIPor5XmiJDnu6novr7lm73lrrblpI3or5XmoIflh4blrabnlJ/lhaznpLpcPC9hXD5cPHNwYW4gY2xhc3M9J25ldydcPm5ld1w8L3NwYW5cPlw8c3BhbiBjbGFzcz0ndGltZSdcPjIwMTctMDUtMTIgXDwvc3Bhblw+XDwvbGlcPlw8bGlcPlw8c3BhbiBjbGFzcz0ndHlwZSdcPlw8L3NwYW5cPlw8YSBocmVmPSdnZ3NtLmFzcHg/ZmJzaj0yMDE1LTA5LTIxIDExOjIwOjMxJnl4cXg9MjAxOC0wOS0zMCcgdGFyZ2V0PSdfYmxhbmsnICAgXD7lrabnlJ/pgInor77lj4rmiJDnu6npl67popjnm7jlhbPmtYHnqItcPC9hXD5cPHNwYW4gY2xhc3M9J25ldydcPm5ld1w8L3NwYW5cPlw8c3BhbiBjbGFzcz0ndGltZSdcPjIwMTUtMDktMjEgXDwvc3Bhblw+XDwvbGlcPlw8bGlcPlw8c3BhbiBjbGFzcz0ndHlwZSdcPlw8L3NwYW5cPlw8YSBocmVmPSdnZ3NtLmFzcHg/ZmJzaj0yMDE0LTA1LTE1IDE1OjUxOjU2Jnl4cXg9MjAxOC0wNS0yNicgdGFyZ2V0PSdfYmxhbmsnICAgXD7lhawg56S6XDwvYVw+XDxzcGFuIGNsYXNzPSduZXcnXD5uZXdcPC9zcGFuXD5cPHNwYW4gY2xhc3M9J3RpbWUnXD4yMDE0LTA1LTE1IFw8L3NwYW5cPlw8L2xpXD5cPGxpXD5cPHNwYW4gY2xhc3M9J3R5cGUnXD5cPC9zcGFuXD5cPGEgaHJlZj0nZ2dzbS5hc3B4P2Zic2o9MjAxNC0wMi0yNSAxMjoxNDowNyZ5eHF4PTIwMTktMDItMjcnIHRhcmdldD0nX2JsYW5rJyAgIFw+5YWz5LqO5Lit5paH5oiQ57up5Y2V572R5LiK6aKE57qm55qE6YCa55+lXDwvYVw+XDxzcGFuIGNsYXNzPSduZXcnXD5uZXdcPC9zcGFuXD5cPHNwYW4gY2xhc3M9J3RpbWUnXD4yMDE0LTAyLTI1IFw8L3NwYW5cPlw8L2xpXD5cPGxpXD5cPHNwYW4gY2xhc3M9J3R5cGUnXD5cPC9zcGFuXD5cPGEgaHJlZj0nZ2dzbS5hc3B4P2Zic2o9MjAxMy0wMy0wOCAxMToyNzoyNiZ5eHF4PTIwNDAtMDMtMzEnIHRhcmdldD0nX2JsYW5rJyAgIFw+572R5LiK6YCJ6K++5q2l6aqkXDwvYVw+XDxzcGFuIGNsYXNzPSduZXcnXD5uZXdcPC9zcGFuXD5cPHNwYW4gY2xhc3M9J3RpbWUnXD4yMDEzLTAzLTA4IFw8L3NwYW5cPlw8L2xpXD47Pj47Oz47dDxwPGw8aW5uZXJodG1sOz47bDw7Pj47Oz47dDxwPGw8aW5uZXJodG1sOz47bDw7Pj47Oz47dDxwPGw8aW5uZXJodG1sOz47bDw7Pj47Oz47Pj47Pj47PtiXlu/a3aZTdEsHUPtXabqnOxmA',
		'tname':"",
		'tbtns':"",
		'tnameXw':"yhdl",
		'tbtnsXw':"yhdl|xwxsdl",
		'txtYhm':userid,
		'txtXm':"",
		'txtMm':password,
		'rblJs':"%D1%A7%C9%FA",		#url码转译'学生'
		'btnDl':"%B5%C7+%C2%BC",	#转译'登录'
	}
	data = urllib.urlencode(loginvalue)
	cookie = cookielib.CookieJar()
	handler=urllib2.HTTPCookieProcessor(cookie)
	opener=urllib2.build_opener(handler)
	response1 = opener.open(url1,data)
	cookies=''
	for item in cookie:
		cookies=item.value
	header = {
		'Host':'218.198.176.112',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding':'gzip, deflate',
		'Referer':'http://218.198.176.112/default6.aspx',
		'Cookie':'ASP.NET_SessionId='+cookies,
		'Connection':'keep-alive',
		'Upgrade-Insecure-Requests':'1',
	}
	values = {
		'xh':userid,
		'xm':nameurl,
		'gnmkdm':'N121603',
	}
	data = urllib.urlencode(values)
	request1 = urllib2.Request(url2,data,header)
	response1 = urllib2.urlopen(request1)
	pages = response1.read().decode('gbk')
	
	fields = re.split(r'<br>',pages)
	pages = ''.join(fields)
	#for line in pages:
	#	re.sub('<br>','',line)
	html = etree.HTML(pages)
	allclass = html.xpath('//table[@id="Table1"]/tr/td')
	m1 = 0
	m2 = 0
	m3 = 0
	m4 = 0
	m5 = 0
	for i in allclass:
		if i.text == '第1节':
			break
		m1 += 1
	for i in allclass:
		if i.text == '第3节':
			break
		m2 += 1
	for i in allclass:
		if i.text == '第5节':
			break
		m3 += 1
	for i in allclass:
		if i.text == "第7节":
			break
		m4 += 1
	for i in allclass:
		if i.text == "第9节":
			break
		m5 += 1
	value = {
		'Pname':html.xpath('//span[@id="Label6"]')[0].text,				#姓名
		'PSchool':html.xpath('//span[@id="Label7"]')[0].text,			#学院
		'PDriection':html.xpath('//span[@id="Label8"]')[0].text,			#专业
		'Pclass':html.xpath('//span[@id="Label9"]')[0].text,				#班级
		'name':html.xpath('//span[@id="Label6"]')[0].text[3:],	#表格标题姓名
		'one12':allclass[m1+1].text,
		'one34':allclass[m2+1].text,
		'one56':allclass[m3+1].text,
		'one78':allclass[m4+1].text,
		'one90':allclass[m5+1].text,
		'two12':allclass[m1+2].text,
		'two34':allclass[m2+2].text,
		'two56':allclass[m3+2].text,
		'two78':allclass[m4+2].text,
		'two90':allclass[m5+2].text,
		'three12':allclass[m1+3].text,
		'three34':allclass[m2+3].text,
		'three56':allclass[m3+3].text,
		'three78':allclass[m4+3].text,
		'three90':allclass[m5+3].text,
		'four12':allclass[m1+4].text,
		'four34':allclass[m2+4].text,
		'four56':allclass[m3+4].text,
		'four78':allclass[m4+4].text,
		'four90':allclass[m5+4].text,
		'five12':allclass[m1+5].text,
		'five34':allclass[m2+5].text,
		'five56':allclass[m3+5].text,
		'five78':allclass[m4+5].text,
		'five90':allclass[m5+5].text,
	}
	return render(request,'cl/data.html',value)
