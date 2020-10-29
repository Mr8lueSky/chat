from django.db import models


# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=2000)
    time = models.TimeField(auto_now=True)