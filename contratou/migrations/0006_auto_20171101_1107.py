# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratou', '0005_auto_20171030_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacaocontratante',
            name='comentario',
            field=models.TextField(default='Teste'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='avaliacaoprofissional',
            name='comentario',
            field=models.TextField(default='Teste'),
            preserve_default=False,
        ),
    ]
