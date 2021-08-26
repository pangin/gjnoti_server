from rest_framework import serializers
from apps.user.models import User

from apps.keywords.models import Keyword
from apps.keywords.serializers import KeywordResponseSerializer, KeywordListSerializer
from apps.univ.models import Univ
from apps.univ.serializers import UnivSerializer


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.Serializer):
    chat_id = serializers.CharField(max_length=100)
    keywords = KeywordListSerializer()
    univ = serializers.CharField(max_length=100)

    def create(self, validated_data):
        univ = Univ.objects.get(name=validated_data['univ'])
        keywords = []
        for name in validated_data['keywords']:
            _keyword, created = Keyword.objects.get_or_create(name=name)
            keywords.append(_keyword)
        user = User.objects.create(chat_id=validated_data['chat_id'], univ=univ)
        for _keyword in keywords:
            user.keywords.add(_keyword)
        return user

    def update(self, instance, validated_data):
        instance.chat_id = validated_data.get('chat_id', instance.chat_id)
        instance.univ = validated_data.get('univ', instance.univ)
        instance.keywords = validated_data.get('keywords', instance.keywords)
        instance.save()
        return instance
