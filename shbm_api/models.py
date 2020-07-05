from django.db import models
from django import forms
from uuid import uuid4
from time import time

class host(models.Model):
    owner = models.ForeignKey('auth.User', related_name='host', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    idstr = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    hostname = models.CharField(max_length=60, default='')
    heartrate = models.BigIntegerField(default=time(), editable=False)
    down = models.BooleanField(default=True, editable=False)
    ip = models.CharField(max_length=60, default='No IP yet', editable=False)
    recipient1 = models.EmailField(default="", verbose_name = "Email to")
    recipient2 = models.EmailField(default="", verbose_name = "Email to (CC)", blank=True)

    def __str__(self):
        return str(self.idstr)
