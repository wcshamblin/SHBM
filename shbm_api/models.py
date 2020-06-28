from django.db import models
from django import forms
from uuid import uuid4
from time import time

class host(models.Model):
    active = models.BooleanField()
    idstr = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    hostname = models.CharField(max_length=60, default='null') # email
    heartrate = models.BigIntegerField(default=time(), editable=False)
    down = models.BooleanField(default=True, editable=False)
    ip = models.CharField(max_length=60, default='null', editable=False)
    def __str__(self):
        return str(self.idstr)
