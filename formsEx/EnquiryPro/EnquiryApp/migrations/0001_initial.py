# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-15 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=20)),
                ('memail', models.EmailField(max_length=20)),
                ('mmobile', models.BigIntegerField()),
                ('mcourse', multiselectfield.db.fields.MultiSelectField(choices=[('py', 'PYTHON'), ('dj', 'DJANGO'), ('ui', 'UI'), ('ra', 'RESTAPI')], max_length=200)),
                ('mtrainer', multiselectfield.db.fields.MultiSelectField(choices=[('RAMYA', 'ramya'), ('SAI', 'sai'), ('KESAV', 'kesav')], max_length=200)),
                ('mbranch', multiselectfield.db.fields.MultiSelectField(choices=[('srnagar', 'SRNAGAR'), ('madpur', 'MADHAPUR'), ('kphb', 'KPHB')], max_length=200)),
                ('mgender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=30)),
                ('mdate', models.DateField(max_length=100)),
            ],
        ),
    ]
