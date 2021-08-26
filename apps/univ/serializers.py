from rest_framework import serializers
from apps.univ.models import Univ


class UnivSerializer(serializers.ModelSerializer):
    class Meta:
        model = Univ
        fields = '__all__'
