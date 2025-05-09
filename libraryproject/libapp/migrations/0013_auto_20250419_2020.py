# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2025-04-19 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0012_digitalresource'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acceptedbookrequest',
            options={'ordering': ['-accepted_date']},
        ),
        migrations.AddField(
            model_name='acceptedbookrequest',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='acceptedbookrequest',
            name='returned_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
