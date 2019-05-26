from rest_framework.serializers import ModelSerializer
from cc import models
from cc.Serializers.DataEnumerationSerializer import DataEnumerationSerializer


class ExecutionDataSerializer(ModelSerializer):
	
	
	class Meta:
		model = models.ExecutionData
		fields = ("id", "Field", "DataGroup", "Value")
