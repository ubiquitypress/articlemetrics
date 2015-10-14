from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.utils import timezone
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view, permission_classes
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from api import serializers

import json
from pprint import pprint

from core import models

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
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
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = models.Publication.objects.all().order_by('-date_published')
    serializer_class = serializers.PublicationSerializer

@api_view(['POST'])
def create_publication(request):
    content = json.loads(request.POST.get('_content'))

    try:
        publisher = models.Publisher.objects.get(name=content.get('publisher_name'))
    except models.Publisher.DoesNotExist:
        return HttpResponse(json.dumps({'response': 'Publisher "%s" not found' % content.get('publisher_name')}), content_type="application/json")

    defaults = {
        'title': content.get('title'),
        'canonical_url': content.get('canonical_url'),
        'canonical_url_two': content.get('canonical_url_two'),
        'date_published': content.get('date_published'),
    }

    publication, created = models.Publication.objects.get_or_create(identifier=content.get('identifier'), publisher=publisher, defaults=defaults)

    print publication, created

    if created:
        json_content = json.dumps({'response': 'New publication created'})
    else:
        json_content = json.dumps({'response': 'Publication updated'})

    return HttpResponse(json_content, content_type="application/json")
