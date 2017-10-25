from django.contrib import admin
from models import *


class PublisherAdmin(admin.ModelAdmin):

    list_display = ('name', 'doi_prefix')
    search_fields = ['name', 'doi_prefix']


class PublicationAdmin(admin.ModelAdmin):

    list_display = ('title', 'identifier', 'publisher')
    search_fields = ('identifier', 'canonical_url')


class TweetAdmin(admin.ModelAdmin):

    list_display = ('publication', 'user', 'url')
    search_fields = ('user', 'url', 'content')
    list_filter = ('publication',)


class QueueAdmin(admin.ModelAdmin):

    list_display = ('publication', 'source')


class CitationAdmin(admin.ModelAdmin):

    list_display = ('publication', 'doi', 'article_title')
    search_fields = ('doi', 'article_title')
    list_filter = ('publication',)


class FacebookAdmin(admin.ModelAdmin):

    list_display = ('publication', 'total_count')
    list_filter = ('publication',)


class WikipediaAdmin(admin.ModelAdmin):

    list_display = ('publication', 'title', 'timestamp')
    list_filter = ('publication',)


admin_list = [
    (Publisher, PublisherAdmin),
    (Publication, PublicationAdmin),
    (Tweet, TweetAdmin),
    (Queue, QueueAdmin),
    (Citation, CitationAdmin),
    (Facebook, FacebookAdmin),
    (Wikipedia, WikipediaAdmin),
    (TwitterCredential,),
]

[admin.site.register(*t) for t in admin_list]
