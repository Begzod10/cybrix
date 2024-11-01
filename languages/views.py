from rest_framework import viewsets, status
from rest_framework.response import Response

from cybrix.functions import QueryParamFilterMixin
from .models import Language, Database, Frameworks
from .seriliazers import LanguageSerializers, DatabaseSerializers, FrameworksSerializers


class LanguageProgramming(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)


class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializers

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)


class FrameworkViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    filter_mappings = {'language': 'language'}
    queryset = Frameworks.objects.all()
    serializer_class = FrameworksSerializers
