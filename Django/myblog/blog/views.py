# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . import models
# Create your views here.

def index(request):
	articles  = models.Article.objects.all()
	articles = articles[::-1]	#最新一篇文章在最后,优先显示新文章
	return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
	article = models.Article.objects.get(pk=article_id)
	talks = models.talk.objects.filter(tid=article_id)
	if request.POST.get('discount'):
		discount = request.POST.get('discount')
		models.talk.objects.create(tid=article_id,discount=discount)
		talks=models.talk.objects.filter(tid=article_id)
		for talk in talks:
			print talk.discount
		return render(request,'blog/article_page.html',{'article':article,'talks':talks})
	return render(request,'blog/article_page.html',{'article':article,'talks':talks})

def edit_page(request,article_id):
	if str(article_id )=='0':
		return render(request,'blog/edit_page.html')
	else:
		article=models.Article.objects.get(pk=article_id)
		return render(request,'blog/edit_page.html',{'article':article})

def	edit_action(request):
	title = request.POST.get('title','TITLE')
	content = request.POST.get('content','CONTENT')
	article_id = request.POST.get('article_id','0')
	talks = models.talk.objects.filter(tid=article_id)
	if article_id=='0':
		models.Article.objects.create(title=title,content=content)
		articles = models.Article.objects.all()
		return render(request,'blog/index.html',{'articles':articles,'talks':talks})
	article = models.Article.objects.get(pk=article_id)
	article.title = title
	article.content = content
	article.save()
	return render(request,'blog/article_page.html',{'article':article,'talks':talks})
