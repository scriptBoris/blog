# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_full',
            field=models.TextField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]
