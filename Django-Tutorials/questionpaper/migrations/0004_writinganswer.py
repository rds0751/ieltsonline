# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-23 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionpaper', '0003_writingtest'),
    ]

    operations = [
        migrations.CreateModel(
            name='WritingAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(default='Writing Test', max_length=100)),
                ('ques1', models.TextField(default='Nothing Written', max_length=1000000)),
            ],
        ),
    ]
