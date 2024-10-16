from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cybrix.functions import CustomResponseMixin
from client_requests.models import ClientRequests
from client_requests.serializers import (
    ClientRequestSerializers
)


class CreateRequestAPIView(CustomResponseMixin, generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ClientRequestSerializers.objects.all()
    serializer_class = ClientRequestSerializers


class RequestUpdateAPIView(CustomResponseMixin, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ClientRequestSerializers.objects.all()
    serializer_class = ClientRequestSerializers


class RequestDeleteAPIView(CustomResponseMixin, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ClientRequestSerializers.objects.all()
    serializer_class = ClientRequestSerializers

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)
