from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from cc.Serializers.UserSerializer import UserSerializer
from cc.Serializers.RoleSerializer import RoleSerializer
from cc import models


class MemberSerializer(ModelSerializer):
	User = UserSerializer(required=False)
	Roles = RoleSerializer(required=False, many=True)
	IsCreator = SerializerMethodField()
	
	
	class Meta:
		model = models.Member
		fields = ("Banned", "User", "Roles", "IsCreator")
	
	
	def get_IsCreator(self, model):
		return model.IsCreator
