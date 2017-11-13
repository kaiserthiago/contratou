# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 13:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contratou', '0012_auto_20171104_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfissionalAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Respostas',
            },
        ),
        migrations.CreateModel(
            name='ProfissionalQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', max_length=20)),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Profissional')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Perguntas ao Profissional',
            },
        ),
        migrations.AddField(
            model_name='profissionalanswer',
            name='profissional_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.ProfissionalQuestion'),
        ),
        migrations.AddField(
            model_name='profissionalanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
