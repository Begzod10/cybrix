from django.db import models

from django.db.models.signals import post_migrate
from django.dispatch import receiver


# Create your models here.
class ClientRequests(models.Model):
    """ center, school, institute ... """
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    telegram_username = models.CharField(max_length=255)
    deleted_status = models.BooleanField(default=False)
