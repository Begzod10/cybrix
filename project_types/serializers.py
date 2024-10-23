from rest_framework import serializers
from .models import ProjectType


class ProjectTypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '__all__'
