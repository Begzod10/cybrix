from rest_framework import serializers

from .models import Language, Frameworks, Database


class FrameworksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Frameworks
        fields = '__all__'


class DatabaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'


class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
