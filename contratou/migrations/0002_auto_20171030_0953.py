# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratou', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['descricao'], 'verbose_name_plural': 'Áreas'},
        ),
        migrations.AlterModelOptions(
            name='profissional',
            options={'ordering': ['nome'], 'verbose_name_plural': 'Profissionais'},
        ),
        migrations.AlterModelOptions(
            name='servico',
            options={'verbose_name_plural': 'Serviços'},
        ),
    ]