from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from cc import models


class CategorySerializer(ModelSerializer):
	
	class Meta:
		model = models.Category
		fields = '__all__'
