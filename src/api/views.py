import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets

from api import serializers
from core import models


class PublicationViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows books to be viewed or edited. """

    queryset = models.Publication.objects.all().order_by('-date_published')
    serializer_class = serializers.PublicationSerializer


@csrf_exempt
def create_publication(request):
    content = request.GET

    try:
        publisher = models.Publisher.objects.get(
            name=content.get('publisher_name')
        )
    except models.Publisher.DoesNotExist:
        return HttpResponse(
            json.dumps({
                'response':
                'Publisher "%s" not found' % content.get('publisher_name')
            }),
            content_type="application/json"
        )

    content.get('canonical_url')
    content.get('canonical_url_two')

    defaults = {
        'title': content.get('title'),
        'canonical_url': content.get('canonical_url'),
        'canonical_url_two': content.get('canonical_url_two'),
        'date_published': content.get('date_published'),
    }

    publication, created = models.Publication.objects.get_or_create(
        identifier=content.get('identifier'),
        publisher=publisher,
        defaults=defaults,
    )

    if created:
        json_content = json.dumps({'response': 'New publication created'})
    else:
        json_content = json.dumps({'response': 'Publication updated'})

    return HttpResponse(json_content, content_type="application/json")
