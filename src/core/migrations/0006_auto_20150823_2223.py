# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150823_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='canonical_url_two',
            field=models.URLField(help_text=b'Full URL with FQDN excluding http://', max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='queue',
            name='source',
            field=models.CharField(max_length=100, choices=[(b'twitter', b'Twitter'), (b'crossref', b'Crossref'), (b'facebook', b'Facebook')]),
        ),
    ]
