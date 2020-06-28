from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from . import views

urlpatterns = [
    re_path(r'^api/v1/hosts/(?P<pk>........-....-....-....-............+)$', # Url to get update or delete a movie
        views.heartbeat.as_view(),
        name='heartbeat'
    ),
]