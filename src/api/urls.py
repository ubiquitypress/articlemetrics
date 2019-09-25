from django.conf.urls import patterns, include, url

from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'publications', views.PublicationViewSet)

urlpatterns = patterns(
    '',
    url(
        r'^create/publication/$',
        'api.views.create_publication',
        name='create_publication'
    ),
    url(
        r'^',
        include(router.urls)
    ),
)
