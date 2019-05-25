from rest_framework.serializers import ModelSerializer
from cc import models
from cc.Serializers.ExecutionDataSerializer import DataFieldSerializer


class DataTypeSerializer(ModelSerializer):
	Fields = DataFieldSerializer(required=False, many=True)
	
	
	class Meta:
		model = models.DataType
		fields = ("id", "Name", "Fields", "Community")
