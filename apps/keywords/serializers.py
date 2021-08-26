from rest_framework import serializers
from apps.keywords.models import Keyword


class KeywordResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class KeywordListSerializer(serializers.ListSerializer):
    child = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Keyword.objects.get_or_create(name=validated_data['name'])


"""
class KeywordUpdateSerializer(serializers.ListSerializer):
    child = serializers.CharField(max_length=150)
    
    def create(self, validated_data):
        return Keyword.objects.get_or_create(name=validated_data['keywords'])
    """
