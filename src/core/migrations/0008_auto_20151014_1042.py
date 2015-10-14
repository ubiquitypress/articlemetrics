# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_wikipedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='source',
            field=models.CharField(max_length=100, choices=[(b'twitter', b'Twitter'), (b'crossref', b'Crossref'), (b'facebook', b'Facebook'), (b'wikipedia', b'Wikipedia')]),
        ),
        migrations.AlterField(
            model_name='wikipedia',
            name='snippet',
            field=models.TextField(max_length=2000),
        ),
    ]
