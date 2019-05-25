from rest_framework.serializers import ModelSerializer
from cc import models


class DataFieldSerializer(ModelSerializer):
    class Meta:
        model = models.ExecutionData
        fields = ("id", "Field", "DataGroup", "Value")
