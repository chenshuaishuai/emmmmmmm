# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from TestModel.models import Test,Contact,Tag
# Register your models here.



#为了让admin管理某个数据模型,应该先注册这个数据模型到admin
#admin.site.register([Test,Contact,Tag])


#只显示name和email的部分
"""
class ContactAdmin(admin.ModelAdmin):
	fields=('name','email')

admin.site.register(Contact,ContactAdmin)
admin.site.register([Test,Tag])
"""

"""
class TagInline(admin.TabularInline):
	model=Tag

class ContactAdmin(admin.ModelAdmin):
	inlines = [TagInline]	#内联.
	fieldsets=(
		['Main',{
			'fields':('name','email'),
		}],
		['Advance',{
			'classes':('collapse',),#css
			'fields':('age',),
		}]
	)

admin.site.register(Contact,ContactAdmin)
admin.site.register([Test])
"""

class ContactAdmin(admin.ModelAdmin):
	list_display=('name','age','email')	#list
	search_fields=('name',)


admin.site.register(Contact,ContactAdmin)
admin.site.register([Test])
