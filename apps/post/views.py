from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.post.models import Post
from apps.post.serializers import PostResponseSerializer, PostCreateSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostResponseSerializer

    def create(self, request, *args, **kwargs):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            post = serializer.create(request.data)
            response_serializer = PostResponseSerializer(post)
            return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid Data'})
