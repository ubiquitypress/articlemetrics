from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'publications', views.PublicationViewSet)

urlpatterns = patterns('',
    url(r'^$', 'api.views.index', name='index'),
    url(r'^create/publication/$', 'api.views.create_publication', name='create_publication'),
    url(r'^', include(router.urls)),
)