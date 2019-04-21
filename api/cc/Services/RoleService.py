import logging


class RoleService(object):
	__instance = None
	__logger = logging.getLogger('RoleService')

	@staticmethod
	def Instance():
		if RoleService.__instance is None:
			RoleService()
		return RoleService.__instance

	def __init__(self):
		if RoleService.__instance is not None:
			raise Exception("RoleService is a singleton, use 'RoleService.Instance()'")
		RoleService.__instance = self
	
	def Get(self, id):
		raise NotImplementedError
	
	def List(self, communityId):
		raise NotImplementedError
	
	def Create(self, name, communityId):
		raise NotImplementedError
	
	def Rename(self, role):
		raise NotImplementedError
