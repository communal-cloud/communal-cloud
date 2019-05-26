from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from cc.Serializers.UserSerializer import UserSerializer
from cc.Serializers.RoleSerializer import RoleSerializer
from cc import models


class MemberSerializer(ModelSerializer):
	User = UserSerializer(required=False)
	Roles = RoleSerializer(required=False, many=True)
	IsCreator = SerializerMethodField("IsCreator")

	class Meta:
		model = models.Member
		fields = ("Deleted", "Banned", "User", "Roles", "IsCreator")
