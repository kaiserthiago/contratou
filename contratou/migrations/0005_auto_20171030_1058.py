# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratou', '0004_auto_20171030_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='foto',
            field=models.ImageField(upload_to='img_profissional'),
        ),
    ]
