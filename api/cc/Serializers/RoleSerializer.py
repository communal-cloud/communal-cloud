from rest_framework.serializers import ModelSerializer
from cc import models


class RoleSerializer(ModelSerializer):
	class Meta:
		model = models.Role
		fields = '__all__'
