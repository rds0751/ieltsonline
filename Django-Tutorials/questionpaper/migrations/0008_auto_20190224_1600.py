# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-24 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionpaper', '0007_readinganswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readinganswer',
            name='ans',
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='test_name',
            field=models.CharField(default='Writing Test', max_length=100),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn0',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn4',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn5',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn_id1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn_id2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn_id3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn_id4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='ysn_id5',
            field=models.IntegerField(null=True),
        ),
    ]
