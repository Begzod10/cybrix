from rest_framework import serializers

from .models import ClientRequests


class ClientRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientRequests
        fields = '__all__'
