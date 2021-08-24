from rest_framework import serializers

from apps.univ.models import Univ
from apps.univ.serializers import UnivResponseSerializer
from apps.keywords.models import Keyword
from apps.keywords.serializers import KeywordResponseSerializer
from apps.post.models import Post


class PostResponseSerializer(serializers.ModelSerializer):
    univ = UnivResponseSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'url', 'univ')


class PostCreateSerializer(serializers.Serializer):
    title = 
