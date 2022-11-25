from django.urls import include, re_path

from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'publications', views.PublicationViewSet)

urlpatterns = [
    re_path(
        r'^create/publication/$',
        views.create_publication,
        name='create_publication'
    ),
    re_path(
        r'^',
        include(router.urls)
    ),
]
