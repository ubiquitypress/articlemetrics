# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151014_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='issue',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='citation',
            name='volume',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='citation',
            name='year',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
