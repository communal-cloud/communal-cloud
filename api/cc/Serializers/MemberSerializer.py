from rest_framework.serializers import ModelSerializer
from cc import models


class MemberSerializer(ModelSerializer):
	class Meta:
		model = models.Member
		fields = '__all__'
