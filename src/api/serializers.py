from rest_framework import serializers

from core import models


class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Publisher
        fields = (
            'name',
            'doi_prefix',
        )


class WikipediaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Wikipedia
        fields = (
            'title',
            'snippet',
            'timestamp',
        )


class CrossrefSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Citation
        fields = (
            'doi',
            'journal_title',
            'article_title',
            'year',
            'volume',
            'issue'
        )


class FacebookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Facebook
        fields = (
            'share_count',
            'like_count',
            'comment_count',
            'click_count',
            'total_count',
        )


class TweetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Tweet
        fields = (
            'content',
            'user',
            'username',
            'profile_image',
            'url',
            'enabled',
            'date',
        )


class PublicationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Publication
        fields = (
            'publisher',
            'title',
            'identifier',
            'canonical_url',
            'canonical_url_two',
            'date_published',
            'wikipedia',
            'crossref',
            'facebook',
            'tweet',
        )

    publisher = PublisherSerializer(
        many=False,
    )
    crossref = CrossrefSerializer(
        many=True,
        source='citation_set',
        required=False,
    )
    wikipedia = WikipediaSerializer(
        many=True,
        source='wikipedia_set',
        required=False,
    )
    facebook = FacebookSerializer(
        many=True,
        source='facebook_set',
        required=False,
    )
    tweet = TweetSerializer(
        many=True,
        source='tweet_set',
        required=False,
    )
