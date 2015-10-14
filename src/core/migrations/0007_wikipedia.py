# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150823_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wikipedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('snippet', models.CharField(max_length=2000)),
                ('timestamp', models.DateTimeField()),
                ('publication', models.ForeignKey(to='core.Publication')),
            ],
        ),
    ]
