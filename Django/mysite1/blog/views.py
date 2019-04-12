# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,JsonResponse,FileResponse
from django.template import loader
from .models import Blog

# Create your views here.

def hello(request):
	return HttpResponse('<html>hello world</html>')

def showBlog(request,blogId):
	t = loader.get_template('blog.html')
	blog = Blog.objects.get(id = blogId)
	context = {'blog':blog}
	html = t.render(context)
	return HttpResponse(html)

def showBlogList(requset):
	t = loader.get_template('blog_list.html')
	blogs = Blog.objects.all()
	context = {'blogs':blogs}
	html = t.render(context)
	return HttpResponse(html)
