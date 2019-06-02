from rest_framework.serializers import ModelSerializer
from cc import models
from cc.Serializers.ExecutionDataSerializer import ExecutionDataSerializer
from cc.Serializers.UserSerializer import UserSerializer


class ExecutionSerializer(ModelSerializer):
	Data = ExecutionDataSerializer(required=False, many=True)
	ExecutedBy = UserSerializer()
	
	class Meta:
		model = models.Execution
		fields = ("id", "Task", "Data", "ExecutedBy")
