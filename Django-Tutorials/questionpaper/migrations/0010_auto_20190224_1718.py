# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-24 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionpaper', '0009_readinganswer_ysn_id0'),
    ]

    operations = [
        migrations.AddField(
            model_name='readinganswer',
            name='sum0',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='sum1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='sum2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='sum3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='sum4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='sum5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='sum_id',
            field=models.IntegerField(null=True),
        ),
    ]