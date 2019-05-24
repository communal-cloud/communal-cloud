from rest_framework import serializers

from cc import models


class CommunitySerializer(serializers.Serializer):
    class Meta:
        model = models.Community
        fields = '__all__'
