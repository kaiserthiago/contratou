# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratou', '0008_auto_20171104_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacaoprofissional',
            name='data_servico',
            field=models.DateField(),
        ),
    ]