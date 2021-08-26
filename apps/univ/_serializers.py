from rest_framework import serializers

from apps.univ.models import Univ


class UnivListSerializer(serializers.ListSerializer):
    child = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Univ.objects.get_or_create(name=validated_data['name'])


class UnivResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Univ
        fields = ('name')
