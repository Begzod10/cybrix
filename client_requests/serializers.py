from rest_framework import serializers

from .models import ClientRequests


class ClientRequestSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = ClientRequests
        fields = ['id', 'name', 'surname', 'phone_number', 'telegram_username']

    def create(self, validated_data):
        return ClientRequests.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
