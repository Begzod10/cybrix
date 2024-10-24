from rest_framework import serializers
from .models import Project, ProjectDocuments


class ProjectSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Project
        fields = '__all__'

    def get_image(self, obj):
        urls = []
        for i in obj.image.all():
            urls.append(i.file.url)
        return urls


class ProjectDocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectDocuments
        fields = '__all__'
