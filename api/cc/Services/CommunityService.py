import logging

from cc.Services.CategoryService import CategoryService
from cc.Services.RoleService import RoleService
from cc.models import Community


class CommunityService(object):
	__instance = None
	__logger = logging.getLogger('CommunityService')
	__categoryService = CategoryService.Instance()
	__roleService = RoleService.Instance()
	
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
		model.save()
		for c in community.get("Categories", u""):
			obj,created = self.__categoryService.GetOrCreate(c)
			model.Categories.add(obj)
		
	
	def CreateStep2(self, community):
		model = Community.objects.get(pk=community.get("Id"))
		model.Purpose = community.get("Purpose", u"")
		model.save()
		for r in community.get("Roles", u""):
			obj,created = self.__roleService.GetOrCreate(r)
			model.Roles.add(obj)

	def Activate(self, community):
		raise NotImplementedError
