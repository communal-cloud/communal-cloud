import logging
from cc.models import ClassEnum
from cc.models import DataType
from cc.models import DataField
from cc.models import DataEnumeration
from cc.models import Community
import json


class DataFieldService(object):
	__instance = None
	__logger = logging.getLogger('DataFieldService')
	
	@staticmethod
	def Instance():
		if DataFieldService.__instance is None:
			DataFieldService()
		return DataFieldService.__instance
	
	def __init__(self):
		if DataFieldService.__instance is not None:
			raise Exception("DataFieldService is a singleton, use 'DataFieldService.Instance()'")
		DataFieldService.__instance = self

	def Create(self, request):
		pass