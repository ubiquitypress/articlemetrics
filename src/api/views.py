import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers, viewsets
from rest_framework import permissions

from api import serializers
from core import models


class JSONResponse(HttpResponse):
    """ An HttpResponse that renders its content into JSON. """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def index(request):
    response_dict = {
        'Message': 'Welcome to the API',
        'Version': '1.0',
        'API Endpoints':
            [],
    }
    json_content = json.dumps(response_dict)

    return HttpResponse(json_content, content_type="application/json")


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
