from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from client_requests.models import ClientRequests
from client_requests.serializers import (
    ClientRequestSerializers
)
from cybrix.functions import CustomResponseMixin


class ClientRequestViewSet(CustomResponseMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ClientRequests.objects.all()
    serializer_class = ClientRequestSerializers

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)
