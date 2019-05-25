from rest_framework.serializers import ModelSerializer
from cc import models
from cc.Serializers.DataFieldSerializer import DataFieldSerializer


class TaskSerializer(ModelSerializer):
	OutputFields = DataFieldSerializer(required=False, many=True)
	InputFields = DataFieldSerializer(required=False, many=True)
	
	
	class Meta:
		model = models.Task
		fields = '__all__'
