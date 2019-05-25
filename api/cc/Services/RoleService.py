import logging

from django.http import JsonResponse

from cc.models import Role, Community


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
		model = Role.objects.get(pk=id)
		return model
	
	# Get roles by communityId
	def GetList(self, communityId):
		community = Community.objects.get(pk=communityId)
		role_list = Role.objects.filter(community=community)
		return role_list
	
	# def Create(self, name, communityId):
	# 	return Role.objects.create(Name=name)
	
	def Update(self, role, id):
		model = Role.objects.get(pk=id)
		if "Name" in role:
			model.Name = role.get("Name", u"")
		model.save()
		
	def Create(self, name, community_id):
		model = Community.objects.get(pk=community_id)
		obj, created = self.GetOrCreate(name)
		model.Roles.add(obj)
	
	def GetOrCreate(self, role):
		model = Role.objects.get_or_create(Name=role)
		return model
	
	def Delete(self, id):
		role = Role.objects.get(pk=id)
		role.delete()
		return JsonResponse(status=200)