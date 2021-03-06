# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171117_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Editor')),
                ('tags', models.ManyToManyField(to='app.tags')),
            ],
        ),
    ]
