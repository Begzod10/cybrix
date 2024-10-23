from rest_framework import serializers
from .models import Project, ProjectDocuments


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectDocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectDocuments
        fields = '__all__'
