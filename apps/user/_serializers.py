from rest_framework import serializers

from apps.user.models import User
from apps.keywords.models import Keyword
from apps.keywords._serializers import KeywordResponseSerializer, KeywordListSerializer
from apps.univ.models import Univ
from apps.univ._serializers import UnivResponseSerializer, UnivListSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['chat_id', 'keywords', 'univ']


class UserCreateSerializer(serializers.Serializer):
    chat_id = serializers.CharField(max_length=100)
    keyword = KeywordListSerializer()
    univ = serializers.CharField(max_length=100, allow_null=True)

    def create(self, validated_data):
        univ, created = Univ.objects.get_or_create(name=validated_data['univ_name'])
        keywords = []
        for name in validated_data['keywords']:
            _keyword = created = Keyword.objects.get_or_create(name=name)
            keywords.append(_keyword)
        user = User.objects.create(name=validated_data['chat_id'], univ=univ)
        for _keyword in keywords:
            user.keywords.add(_keyword)
        return user

    def update(self, instance, validated_data):
        return User.objects.update(**validated_data)
