import logging
from cc.models import ClassEnum
from cc.models import DataType
from cc.models import DataField
from cc.models import DataEnumeration
from cc.models import Community
import json


class DataService(object):
	__instance = None
	__logger = logging.getLogger('DataService')
	
	@staticmethod
	def Instance():
		if DataService.__instance is None:
			DataService()
		return DataService.__instance
	
	def __init__(self):
		if DataService.__instance is not None:
			raise Exception("DataService is a singleton, use 'DataService.Instance()'")
		DataService.__instance = self
	
	def getEnum(self):
		return {i.name: i.value for i in ClassEnum}
	
	def createDataType(self, request, id):
		model = DataType()
		model.Name = request.get("Name", u"")
		model.Community = Community.objects.get(pk=id)
		model.save()
		self.createDataField({
			"Name": "Identifier",
			"Class": ClassEnum.String.value
		}, model)
		return model
	
	def createDataField(self, request, datatype):
		if "Enumerations" in request:
			for e in request.get("Enumerations", u""):
				for key, value in e.items():
					datafield = DataField.objects.create(Name=request.get("Name", u""), Type=request.get("Class", u""))
					datatype.Fields.add(datafield)
					newenum = DataEnumeration.objects.create(Name=value, Value=key)
					datafield.Enumerations.add(newenum)
		else:
			datafield = DataField.objects.create(
				Name=request.get("Name", u""),
				Type=request.get("Class", ClassEnum.NotSpecified.value)
			)
			datatype.Fields.add(datafield)
