from django.db import models
from datetime import datetime
# Create your models here.


class report(models.Model):
    name = models.CharField(max_length=70, null=True, blank=True)
    email = models.CharField(max_length=70, null=True, blank=True)
    text = models.TextField( null=True, blank=True)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name    