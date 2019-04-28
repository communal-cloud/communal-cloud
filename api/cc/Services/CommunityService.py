import logging

from cc.Services.CategoryService import CategoryService
from cc.models import Community


class CommunityService(object):
	__instance = None
	__logger = logging.getLogger('CommunityService')
	__categoryService = CategoryService.Instance()
	
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
		model = Community()
		model.Name = community.get("Name", u"")
		model.Description = community.get("Description", u"")
		model.Categories=[]
		for c in community.Categories:
			category = self.__categoryService.GetOrCreate(c)
			model.Categories.append(category)
			
		

	def Activate(self, community):
		raise NotImplementedError
