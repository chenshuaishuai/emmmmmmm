# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
#from TestModel.models import Test
from django.shortcuts import render_to_response
import MySQLdb

def hello(request):
	context		= {}
	context['hello'] = 'Hello world!'
	return render(request,'hello.html',context)
	#return HttpResponse("Hello world!")

def book_list(request):
	db = MySQLdb.connect(user='me',db='mydb',passwd='secret',host='localhost')
	cursor = db.cursor()
	cursor.excute('SELECT name FROM books ORDER BY name')
	names=[row[0] for row in cursor.fetchall()]
	db.close()
	return render_to_response('book_list.html',{'names':names})
