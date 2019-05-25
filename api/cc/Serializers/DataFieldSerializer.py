from rest_framework.serializers import ModelSerializer
from cc import models


class DataFieldSerializer(ModelSerializer):
    class Meta:
        model = models.DataField
        fields = ("id", "Name", "Type", "Enumerations", "Save", "Parameters")
