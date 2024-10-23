from rest_framework import viewsets, status
from rest_framework.response import Response
from cybrix.functions import QueryParamFilterMixin
from .models import ProjectType
from .serializers import ProjectTypesSerializers


class ProjectTypeViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    filter_mappings = {
        'status': 'status'
    }
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypesSerializers

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)
