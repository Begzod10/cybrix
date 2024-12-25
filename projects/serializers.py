from rest_framework import serializers

from languages.seriliazers import LanguageSerializers, FrameworksSerializers, DatabaseSerializers,Frameworks,Language,Database
from .models import Project, ProjectDocuments


class ProjectSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(required=False)
    # framework = serializers.PrimaryKeyRelatedField(many=True,queryset=Frameworks.objects.all())
    # language = serializers.PrimaryKeyRelatedField(many=True,queryset=Language.objects.all())
    # database = serializers.PrimaryKeyRelatedField(many=True,queryset=Database.objects.all())

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
    language = LanguageSerializers(many=True, read_only=True)
    framework = FrameworksSerializers(many=True, read_only=True)
    database = DatabaseSerializers(many=True, read_only=True)
    image = serializers.SerializerMethodField()


    class Meta(ProjectSerializers.Meta):
        fields = ['id', 'name','image', 'description', 'registered_at', 'deleted_status', 'finishing_date',
                  'project_type', 'project_url', 'language', 'framework', 'database']
        read_only_fields = ['id', 'registered_at']
    def get_image(self, obj):
        urls = []
        for i in obj.image.all():
            urls.append({'id': i.pk, 'url': i.file.url})
        return urls