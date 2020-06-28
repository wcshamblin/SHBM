from django.db import models
from uuid import uuid4

class host(models.Model):
    idstr = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    hostname = models.CharField(max_length=60, default='null') # email

    def __str__(self):
        return str(self.idstr)