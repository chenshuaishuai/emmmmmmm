# -*- coding:utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test


def testdb(request):
	test1 = Test.objects.get(id=1)	#准备删除id=1的数据
	test1.delete()
		#等价操作:
		#Test.objects.filter(id=1).delete()
		#test.objects.all().delete()	#删除所有数据
	return HttpResponse("<p>删除成功</p>")



	"""
	test1=Test.objects.get(id=1)
	test1.name = "w3cschoolW3Cschool教程"
	test1.save()
		#等价操作:
		#Test.objects.filter(id=1).update(name='w3cschoolW3Cschool教程')
		#修改所有的列
		#Test.objects.all().update(name='w3cschoolW3Cschool教程')
	return HttpResponse("<p>修改成功</p>")
	"""
	
	
	
	
	"""
	response = ""
	response1= ""	#初始化
	list=Test.objects.all()	#提取数据库中的所有数据 相当于 select * from
	response2=Test.objects.filter(id=1)	#filter相当于 where 可以设置条件过滤
	response3=Test.objects.get(id=1)	#获取单个对象
	Test.objects.order_by('name')[0:2]	#限制返回的数据. offset 0 limit 2;
	Test.objects.order_by("id")	#数据排序
	Test.objects.filter(name="w3cschool.cn").order_by("id") #可以连续对数据库操作.
	for var in list:
		response1 += var.name + " "
	response = response1
	return HttpResponse("<p>" + response  + "</p>")
	"""
