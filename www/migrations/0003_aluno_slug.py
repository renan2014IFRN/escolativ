# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_aluno_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
