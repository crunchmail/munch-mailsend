# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgainAnotherMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_mail', to='core.RawMail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnotherMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_anothermail', to='core.RawMail')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
