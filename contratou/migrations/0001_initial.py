# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='AvaliacaoContratante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.IntegerField()),
                ('campo2', models.IntegerField()),
                ('campo3', models.IntegerField()),
                ('campo4', models.IntegerField()),
                ('campo5', models.IntegerField()),
            ],
            options={
                'ordering': ['contratante', 'profissional'],
            },
        ),
        migrations.CreateModel(
            name='AvaliacaoProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.IntegerField()),
                ('campo2', models.IntegerField()),
                ('campo3', models.IntegerField()),
                ('campo4', models.IntegerField()),
                ('campo5', models.IntegerField()),
            ],
            options={
                'ordering': ['profissional', 'contratante'],
            },
        ),
        migrations.CreateModel(
            name='Contratante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(blank=True, max_length=14)),
                ('rg', models.IntegerField(blank=True)),
                ('orgao_expeditor', models.CharField(blank=True, max_length=15)),
                ('data_nascimento', models.DateField()),
                ('logradouro', models.CharField(max_length=255)),
                ('complemento', models.CharField(blank=True, max_length=50)),
                ('cidade', models.CharField(max_length=150)),
                ('uf', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], default='RO', max_length=20)),
                ('cep', models.CharField(max_length=10)),
                ('email', models.CharField(blank=True, max_length=150)),
                ('telefone', models.CharField(max_length=15)),
                ('foto', models.ImageField(blank=True, upload_to='img_profissional')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(blank=True, max_length=14)),
                ('rg', models.IntegerField(blank=True)),
                ('orgao_expeditor', models.CharField(blank=True, max_length=15)),
                ('data_nascimento', models.DateField()),
                ('logradouro', models.CharField(max_length=255)),
                ('complemento', models.CharField(blank=True, max_length=50)),
                ('cidade', models.CharField(max_length=150)),
                ('uf', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], default='RO', max_length=20)),
                ('cep', models.CharField(max_length=10)),
                ('email', models.CharField(blank=True, max_length=150)),
                ('telefone', models.CharField(max_length=15)),
                ('foto', models.ImageField(blank=True, upload_to='img_profissional')),
                ('area', models.ManyToManyField(to='contratou.Area')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(blank=True)),
                ('data', models.DateField()),
                ('contratante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Contratante')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Profissional')),
            ],
        ),
        migrations.AddField(
            model_name='avaliacaoprofissional',
            name='contratante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Contratante'),
        ),
        migrations.AddField(
            model_name='avaliacaoprofissional',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Profissional'),
        ),
        migrations.AddField(
            model_name='avaliacaoprofissional',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Servico'),
        ),
        migrations.AddField(
            model_name='avaliacaocontratante',
            name='contratante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Contratante'),
        ),
        migrations.AddField(
            model_name='avaliacaocontratante',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Profissional'),
        ),
        migrations.AddField(
            model_name='avaliacaocontratante',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Servico'),
        ),
        migrations.AddField(
            model_name='area',
            name='segmento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratou.Segmento'),
        ),
    ]
