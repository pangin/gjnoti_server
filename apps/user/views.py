from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.user.models import User
from apps.user.serializers import UserResponseSerializer, UserCreateSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserResponseSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            response_serializer = UserResponseSerializer(user)
            return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid Data'})

    def partial_update(self, request, *args, **kwargs):
        user_serializer = UserCreateSerializer(data=request.data, partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.update(User.objects.get(chat_id=request.data['chat_id']), request.data)
            response_serializer = UserResponseSerializer(user)
            return Response(data=response_serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response({'error': 'Invalid Data'})
