from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from . import views

urlpatterns = [
    re_path(r'^hosts/(?P<pk>........-....-....-....-............+)$',
        views.heartbeat.as_view(),
        name='heartbeat'
    ),
    # path('hosts/',
    # 	views.createhost.as_view(),
    # 	name='createhost')
]