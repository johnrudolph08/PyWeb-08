# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-23 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='myblog.Category'),
        ),
    ]
