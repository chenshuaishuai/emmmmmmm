# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_talk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='discount',
        ),
    ]
