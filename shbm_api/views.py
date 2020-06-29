from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import host
from .serializers import hostserializer
from time import time

class heartbeat(RetrieveUpdateDestroyAPIView):
    http_method_names = ['get']

    def get_queryset(self, pk):
        try:
            req = host.objects.get(pk=pk)
        except host.DoesNotExist:
            raise Http404("No host matches this ID")
        return req

    def get(self, request, pk):
        try:
            req = self.get_queryset(pk)
        except Http404 as error:
            return Response("404", status=status.HTTP_404_NOT_FOUND)
        req.down = False
        req.heartrate = time()
        req.ip = self.get_client_ip(request)
        req.save(update_fields=['down', 'heartrate', 'ip'])
        return Response("OK", status=status.HTTP_200_OK)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

# class createhost(RetrieveUpdateDestroyAPIView):
#     http_method_names = ['post']
#     def post(self,request):
#         serializer = hostserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data["idstr"], status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)