# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible#装饰器允许写这样的方法去兼容python3
class Question(models.Model):
	question_text = models.CharField(max_length=200) #CharField表示字符字段.这个类需要给它提供一个max_length参数.
	pub_date = models.DateTimeField('date published')#DateTimeField表示时间维度.
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
								#这告诉Django每个字段拥有什么类型的数据.
	def was_published_recently(self):
		now = timezone.now()
		return now-datetime.timedelta(days=1)<=self.pub_date<=now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
#foreignkey告诉django每个choice都有一个相关的Question.Django支持所有常见的数据库关系,多对一,多对多和一对一.
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

def was_published_recently(self):
	now = timezone.now()
	return now-datetime.timedelta(days=1) <= self.pub_date <= now
