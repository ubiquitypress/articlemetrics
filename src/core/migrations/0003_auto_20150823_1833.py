# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_publication_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TwitterCredentials',
            new_name='TwitterCredential',
        ),
    ]
