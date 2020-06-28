from django.shortcuts import render
from uuid import uuid4
import heartmonitor
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import host
from .serializers import hostserializer

class heartbeat(RetrieveUpdateDestroyAPIView):
    http_method_names = ['get']

    def get_queryset(self, pk):
        try:
            req = host.objects.get(pk=pk)
        except host.DoesNotExist:
            raise Http404("No WTB matches this ID")
        return req

    def get(self, request, pk):
        try:
            req = self.get_queryset(pk)
        except Http404 as error:
            return Response("404", status=status.HTTP_404_NOT_FOUND)
        serializer = hostserializer(req)
        print("Hostname:", serializer.data['hostname'])
        return Response("OK", status=status.HTTP_200_OK)
