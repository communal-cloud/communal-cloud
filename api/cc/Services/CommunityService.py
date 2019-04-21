import logging


class CommunityService(object):
	__instance = None
	__logger = logging.getLogger('CommunityService')
	
	@staticmethod
	def Instance():
		if CommunityService.__instance is None:
			CommunityService()
		return CommunityService.__instance
	
	def __init__(self):
		if CommunityService.__instance is not None:
			raise Exception("CommunityService is a singleton, use 'CommunityService.Instance()'")
		CommunityService.__instance = self
	
	def Get(self, id):
		raise NotImplementedError
	
	def GetRecent(self, count):
		raise NotImplementedError
	
	def GetPopular(self, count):
		raise NotImplementedError

	def Create(self, community):
		raise NotImplementedError

	def Activate(self, community):
		raise NotImplementedError
