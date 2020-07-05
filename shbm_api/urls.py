from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from SHBM import settings

urlpatterns = [
    path('hosts/create/', views.CreateHost.as_view(), name='CreateHost'),

	re_path(r'^hosts/delete/(?P<pk>........-....-....-....-............+)$', views.DeleteHost.as_view(), name='DeleteHost'),
    re_path(r'^heartbeat/(?P<pk>........-....-....-....-............+)$',
        views.HeartBeat.as_view(),
        name='HeartBeat'
    ),
    re_path(r'^hosts/(?P<pk>........-....-....-....-............+)$',
        views.EditHost.as_view(),
        name='EditHost'
    ),
    path('hosts/', views.Hosts.as_view(), name='Hosts'),
    path('signup/', views.SignUp.as_view(), name='SignUp'),
    path('logout/', views.Logout.as_view(), name='Logout'),
    path('login/', views.Login.as_view(), name='Login'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('signup/',
    #     views.signup.as_view(),
    #     name='signup'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()