from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from cc import models


class CommunitySerializer(ModelSerializer):
    class Meta:
        model = models.Community
        fields = '__all__'
