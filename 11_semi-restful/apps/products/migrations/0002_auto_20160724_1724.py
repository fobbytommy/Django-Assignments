# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 00:24
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('productManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
