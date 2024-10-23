from rest_framework import viewsets, status
from rest_framework.response import Response

from projects.models import Project, ProjectDocuments
from projects.serializers import ProjectSerializers, ProjectDocumentsSerializers


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)


class ProjectDocumentsViewSet(viewsets.ModelViewSet):
    queryset = ProjectDocuments.objects.all()
    serializer_class = ProjectDocumentsSerializers

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)

    def get_queryset(self):
        if self.request.method == 'GET':
            return self.queryset.filter(deleted_status=False, project=self.kwargs['project_pk'])
