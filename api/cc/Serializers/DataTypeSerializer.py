from rest_framework.serializers import ModelSerializer
from cc import models


class DataTypeSerializer(ModelSerializer):
    class Meta:
        model = models.DataType
        fields = ("id", "Name", "Fields", "Community")
