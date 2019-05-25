import logging
from cc.models import DataType


class DataTypeService(object):
	__instance = None
	__logger = logging.getLogger('DataTypeService')
	
	@staticmethod
	def Instance():
		if DataTypeService.__instance is None:
			DataTypeService()
		return DataTypeService.__instance
	
	def __init__(self):
		if DataTypeService.__instance is not None:
			raise Exception("DataTypeService is a singleton, use 'DataTypeService.Instance()'")
		DataTypeService.__instance = self
	
	def GetByCommunity(self, communityId):
		list = DataType.objects.filter(Community_id=communityId)
		return list