# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-17 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=18, verbose_name='年龄'),
        ),
    ]