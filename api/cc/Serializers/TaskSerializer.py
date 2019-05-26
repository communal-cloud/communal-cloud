from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from cc import models
from cc.Serializers.DataFieldSerializer import DataFieldSerializer
from cc.Serializers.RoleSerializer import RoleSerializer
from cc.Serializers.UserSerializer import UserSerializer


class TaskSerializer(ModelSerializer):
	OutputFields = DataFieldSerializer(required=False, many=True)
	InputFields = DataFieldSerializer(required=False, many=True)
	AssignedUsers = UserSerializer(required=False, many=True)
	AssignedRoles = RoleSerializer(required=False, many=True)
	Predecessors = SerializerMethodField()
	
	class Meta:
		model = models.Task
		fields = '__all__'
	
	
	def get_Predecessors(self, obj):
		if obj.Predecessors.all() is not None:
			list = []
			for predecessor in obj.Predecessors.all():
				list.append(TaskSerializer(predecessor).data)
			return list
		else:
			return None