# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-20 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listening', '0001_initial'),
        ('questionpaper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeningTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(default='Listening Test', max_length=100)),
                ('ques1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Listening1', to='listening.AudioMain')),
                ('ques2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Listening2', to='listening.AudioMain')),
                ('ques3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Listening3', to='listening.AudioMain')),
                ('ques4', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Listening4', to='listening.AudioMain')),
            ],
        ),
    ]
