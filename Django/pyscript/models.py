# models.py (the database tables)

from django.db import models

class Book(models.Model):
	name = models.CharField(max_length=50)
	pub_date = models.DateFiled()
