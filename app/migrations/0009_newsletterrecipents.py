# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_tags_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
