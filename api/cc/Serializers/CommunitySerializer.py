from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from cc import models


class CommunitySerializer(ModelSerializer):
	MemberCount = SerializerMethodField()
	
	
	class Meta:
		model = models.Community
		fields = '__all__'
	
	
	def get_MemberCount(self, model):
		return model.member_set.count()
