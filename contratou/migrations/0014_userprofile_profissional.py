# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contratou', '0013_auto_20171113_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profissional',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='contratou.Profissional'),
            preserve_default=False,
        ),
    ]
