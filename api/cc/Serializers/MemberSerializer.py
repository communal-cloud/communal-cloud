from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from cc import models


class MemberSerializer(ModelSerializer):
	IsCreator = SerializerMethodField("IsCreator")
	class Meta:
		model = models.Member
		fields = '__all__'
