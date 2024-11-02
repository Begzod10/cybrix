from rest_framework import serializers

from languages.seriliazers import LanguageSerializers, FrameworksSerializers, DatabaseSerializers
from .models import Project, ProjectDocuments


class ProjectSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Project
        fields = '__all__'

    def get_image(self, obj):
        urls = []
        for i in obj.image.all():
            urls.append({'id': i.pk, 'url': i.file.url})
        return urls


class ProjectDocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectDocuments
        fields = '__all__'


class ProjectDetailSerializer(ProjectSerializers):
    programming_language = LanguageSerializers(many=True, read_only=True)
    framework = FrameworksSerializers(many=True, read_only=True)
    database = DatabaseSerializers(many=True, read_only=True)

    class Meta(ProjectSerializers.Meta):
        fields = ['id', 'name', 'description', 'registered_at', 'deleted_status', 'finishing_date',
                  'project_type', 'project_url', 'programming_language', 'framework', 'database']
        read_only_fields = ['id', 'registered_at']
