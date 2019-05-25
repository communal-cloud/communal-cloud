from rest_framework.serializers import ModelSerializer
from cc import models


class DataEnumerationSerializer(ModelSerializer):
    class Meta:
        model = models.DataEnumeration
        fields = ("id", "Name", "Value")
