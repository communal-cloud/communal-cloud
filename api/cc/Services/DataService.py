import logging
from cc.models import ClassEnum
from cc.models import DataType
from cc.models import DataField

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

	def createDataType(self,request):
		return DataType.objects.create(Name=request.get("Name",u""))

	def createDataField(self,request,datatype):
		datafield=DataField.objects.create(Name=request.get("Name",u""), Type=request.get("Class",u""))
		datatype.Fields.add(datafield)
