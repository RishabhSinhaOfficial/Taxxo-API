# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20170228_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='Accounts',
        ),
        migrations.RemoveField(
            model_name='company',
            name='maintain_only',
        ),
        migrations.AlterField(
            model_name='company',
            name='books_beginning_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='financial_year_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='show_amounts_in_millions',
            field=models.BooleanField(),
        ),
    ]
