import logging


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