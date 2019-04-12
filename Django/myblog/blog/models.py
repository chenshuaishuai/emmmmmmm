# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
#from . import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=32,default='Title')
	content = models.TextField(null=True)
	pub_time = models.DateTimeField(default=datetime.now)
	def __unicode__(self):
		return self.title

class talk(models.Model):
	tid = models.IntegerField(null=True)
	discount = models.TextField(null=True)
	def __unicode__(self):
		return self.tid
