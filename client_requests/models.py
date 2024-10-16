from django.db import models


# Create your models here.
class ClientRequests(models.Model):
    """ center, school, institute ... """
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    telegram_username = models.CharField(max_length=255)
    deleted_status = models.BooleanField(default=False)
