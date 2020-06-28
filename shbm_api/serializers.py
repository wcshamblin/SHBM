from rest_framework import serializers
from django.contrib.auth.models import User
from .models import host

class hostserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = host
        fields = ('idstr', 'host')
