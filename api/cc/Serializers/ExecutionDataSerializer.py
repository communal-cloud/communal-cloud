from rest_framework.serializers import ModelSerializer
from cc import models
from cc.Serializers.DataEnumerationSerializer import DataEnumerationSerializer


class DataFieldSerializer(ModelSerializer):
	Enumerations = DataEnumerationSerializer(required=False, many=True)
	
	
	class Meta:
		model = models.DataField
		fields = ("id", "Name", "Type", "Enumerations", "Parameters", "Saved")
