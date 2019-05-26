import logging
from cc.models import ClassEnum
from cc.models import DataType
from cc.models import DataField
from cc.models import DataEnumeration
from cc.models import Community
from cc.models import DataEnumeration
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
		model.Community_id = id
		model.save()
		
		self.createDataField({
			"Name": "Identifier",
			"Class": ClassEnum.String.value
		}, model)
		return model
	
	def updateDataType(self, dataTypeId, updateData):
		dataTypeToUpdate = DataType.objects.get(pk = dataTypeId)
		dataTypeToUpdate.Name = updateData.get("Name")
		dataTypeToUpdate.save()
		return dataTypeToUpdate

	def createDataField(self, request, datatype):
		if "Parameters" in request:
			parameters = request["Parameters"]
		else:
			parameters = "{}"

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
				Type=request.get("Class", ClassEnum.NotSpecified.value),
				Parameters = parameters
			)
			datatype.Fields.add(datafield)
	
	def updateDataFields(self, datatype, currentDataFieldList, dataFieldListToUpdate):
		for currentDataField in currentDataFieldList:
			currentDataFieldExistsInUpdateList = any(dataField["id"] == currentDataField.pk for dataField in dataFieldListToUpdate)
			if(currentDataFieldExistsInUpdateList):
				dataFieldToUpdate = [dataField for dataField in dataFieldListToUpdate if dataField["id"] == currentDataField.pk][0]
				self.updateDataField(currentDataField, dataFieldToUpdate)
				dataFieldListToUpdate.remove(dataFieldToUpdate)
			else:
				currentDataField.delete()
			
		if (len(dataFieldListToUpdate) > 0):
			for dataFieldToUpdate in dataFieldListToUpdate:
				self.createNewDataField(datatype, dataFieldToUpdate)
			
	def updateDataField(self, currentDataField, dataFieldToUpdate):
		if ("Name" in dataFieldToUpdate.keys()):
			currentDataField.Name = dataFieldToUpdate["Name"]

		if ("Class" in dataFieldToUpdate.keys()):
			currentDataField.Type = dataFieldToUpdate["Class"]

		for enumeration in currentDataField.Enumerations.all():
				enumeration.delete()
		if ("Enumerations" in dataFieldToUpdate.keys()):
			for enumerationToAdd in dataFieldToUpdate["Enumerations"]:
				self.createNewEnumeration(currentDataField, enumerationToAdd)
		
		currentDataField.save()

	def createNewDataField(self, datatype, dataFieldToCreate):
		datafield = DataField.objects.create(Name=dataFieldToCreate["Name"], Type=dataFieldToCreate["Class"])
		datatype.Fields.add(datafield)

	def createNewEnumeration(self, dataField, enumerationToUpdate):
		for name in enumerationToUpdate:
			value = enumerationToUpdate[name]
			enumeration = DataEnumeration.objects.create(Name=name, Value=value)
			dataField.Enumerations.add(enumeration)