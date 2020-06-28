from django.shortcuts import render
from uuid import uuid4
import heartmonitor

class heartbeat(RetrieveUpdateDestroyAPIView):
    http_method_names = ['get']
    def get(self, request, pk):
    	print("hi lol")
    	return Response("OK", status=status.HTTP_200_OK)