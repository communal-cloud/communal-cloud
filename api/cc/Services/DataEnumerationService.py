import logging
from cc.models import ClassEnum
from cc.models import DataType
from cc.models import DataField
from cc.models import DataEnumeration
from cc.models import Community
import json


class DataEnumerationService(object):
	__instance = None
	__logger = logging.getLogger('DataEnumerationService')
	
	@staticmethod
	def Instance():
		if DataEnumerationService.__instance is None:
			DataEnumerationService()
		return DataEnumerationService.__instance
	
	def __init__(self):
		if DataEnumerationService.__instance is not None:
			raise Exception("DataEnumerationService is a singleton, use 'DataEnumerationService.Instance()'")
		DataEnumerationService.__instance = self

	def Create(self, request):
		pass