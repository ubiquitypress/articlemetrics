# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doi', models.CharField(max_length=200)),
                ('journal_title', models.CharField(max_length=2000)),
                ('article_title', models.CharField(max_length=2000)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('volume', models.IntegerField(null=True, blank=True)),
                ('issue', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('click_count', models.IntegerField(default=0)),
                ('total_count', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(help_text=b'Should be a doi, eg. 10.5334/cg.aa', max_length=200)),
                ('canonical_url', models.URLField(help_text=b'Full URL with FQDN excluding http://', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Publisher like Ubiquity Press or University of California Press', max_length=300)),
                ('doi_prefix', models.CharField(help_text=b"Publisher's CrossRef prefix", max_length=20)),
                ('crossref_username', models.CharField(max_length=100, null=True, blank=True)),
                ('crossref_password', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('user', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('profile_image', models.CharField(max_length=400)),
                ('url', models.URLField()),
                ('enabled', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('publication', models.ForeignKey(to='core.Publication')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterCredentials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consumer_key', models.CharField(max_length=300)),
                ('consumer_secret', models.CharField(max_length=300)),
                ('access_token', models.CharField(max_length=300)),
                ('access_token_secret', models.CharField(max_length=300)),
                ('last_used', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='publisher',
            field=models.ForeignKey(to='core.Publisher'),
        ),
        migrations.AddField(
            model_name='facebook',
            name='publication',
            field=models.ForeignKey(to='core.Publication'),
        ),
        migrations.AddField(
            model_name='citation',
            name='publication',
            field=models.ForeignKey(to='core.Publication'),
        ),
    ]
