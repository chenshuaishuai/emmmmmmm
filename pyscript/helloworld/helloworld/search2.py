# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import * 
#from django.middleware import csrf
import django.views.decorators.csrf

def search_post(request):
	ctx = {}
	ctx.update(csrf(request))
	if request.POST:
		ctx['rlt'] = request.POST['q']
	return render(request,"post.html",ctx)
