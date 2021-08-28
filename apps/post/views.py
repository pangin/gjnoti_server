from django.shortcuts import render

from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from apps.post.models import Post
from apps.post.serializers import PostResponseSerializer, PostCreateSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostResponseSerializer

    def list(self, request, *args, **kwargs):
        new = self.request.query_params.get('new')
        univ = self.request.query_params.get('univ')
        if new and univ:
            queryset = Post.objects.filter(new=new, univ=univ).all()
            response_serializer = PostResponseSerializer(queryset, many=True)
            return Response(data=response_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            post = serializer.create(request.data)
            response_serializer = PostResponseSerializer(post)
            return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid Data'})
