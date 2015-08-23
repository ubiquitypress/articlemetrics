# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150823_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=100, choices=[(b'twitter', b'Twitter'), (b'crossref', b'Crossref')])),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='date_published',
            field=models.DateField(default=datetime.datetime(2015, 8, 23, 18, 50, 37, 875608, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='queue',
            name='publication',
            field=models.ForeignKey(to='core.Publication'),
        ),
    ]
