from rest_framework import serializers

from apps.post.models import Post
from apps.univ.models import Univ
from apps.univ.serializers import UnivSerializer


class PostResponseSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)
    url = serializers.CharField(max_length=150)
    univ = UnivSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    url = serializers.CharField(max_length=150)
    univ = serializers.CharField(max_length=100)

    def create(self, validated_data):
        univ = Univ.objects.get(name=validated_data['univ'])
        post = Post.objects.create(title=validated_data['title'], url=validated_data['url'], univ=univ)
        return post
