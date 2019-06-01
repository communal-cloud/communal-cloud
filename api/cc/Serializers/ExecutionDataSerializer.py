from rest_framework.fields import SerializerMethodField
from rest_framework.relations import RelatedField
from rest_framework.serializers import ModelSerializer, Serializer
from cc import models
from cc.Serializers.DataEnumerationSerializer import DataEnumerationSerializer
from cc.models import ClassEnum


class ExecutionDataSerializer(ModelSerializer):
	FieldName = SerializerMethodField()
	
	
	class Meta:
		model = models.ExecutionData
		fields = ("id", "Field", "FieldName", "DataGroup", "Value")
	
	
	def get_FieldName(self, obj):
		return u"{0} ({1})".format(obj.Field.Name, ClassEnum(obj.Field.Type).name)


class GroupedExecutionDataSerializer(Serializer):
	Items = SerializerMethodField()
	
	def get_Items(self, obj):
		list = []
		for group in obj:
			list.append(ExecutionDataSerializer(group, many=True).data)
		return list
