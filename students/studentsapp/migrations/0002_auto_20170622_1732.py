# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cBirthday',
            field=models.DateField(blank=True, default=''),
        ),
    ]
