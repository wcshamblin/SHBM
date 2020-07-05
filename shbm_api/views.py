from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import host
from .serializers import hostserializer
from time import time
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
class HeartBeat(RetrieveUpdateDestroyAPIView):
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


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')

class Logout(LogoutView):
    success_url = reverse_lazy('login')

class Hosts(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return None
        return host.objects.filter(owner=self.request.user)
    model = host
    template_name = 'hosts.html'  # Specify your own template name/location

class CreateHost(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    model = host
    fields = ["active", "hostname", "recipient1", "recipient2"]
    success_url = "/hosts/"
    template_name = "createhost.html"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class Host(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = host
    template_name = 'host.html'

class DeleteHost(LoginRequiredMixin, generic.DeleteView):
    login_url = '/login/'
    model = host
    success_url = "/hosts/"

class EditHost(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    model = host
    success_url = "/hosts/"
    fields = ["active", "hostname", "recipient1", "recipient2"]
    template_name = 'host.html'



# class createhost(RetrieveUpdateDestroyAPIView):
#     http_method_names = ['post']
#     def post(self,request):
#         serializer = hostserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data["idstr"], status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)