from rest_framework.serializers import ModelSerializer
from cc import models


class DataFieldSerializer(ModelSerializer):
    class Meta:
        model = models.DataField
        fields = '__all__'
