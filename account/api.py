from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework import status
# Create your views here.

from rest_framework import viewsets

from account.models import User
from account.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):
        ser_data = UserSerializer(instance=self.queryset, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        # custom permisstions in viewsets
        if user != request.user:
            return Response({'permission denied': 'you are not the owner'})
        user.is_active = False
        user.save()
        return Response({'message': 'user deactivated'})