from django.shortcuts import render

from rest_framework import viewsets
from apps.keywords.models import Keyword
from apps.keywords.serializers import KeywordResponseSerializer


# Create your views here.
class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordResponseSerializer
