import logging
from django.db.models import Q
from cc.Services.RoleService import RoleService
from cc.models import Member, Community
from cc.models import Execution, Task, ExecutionData, DataField, DataType, TaskType


class MemberService(object):
	__instance = None
	__logger = logging.getLogger('MemberService')
	__roleService = RoleService.Instance()
	
	@staticmethod
	def Instance():
		if MemberService.__instance is None:
			MemberService()
		return MemberService.__instance
	
	def __init__(self):
		if MemberService.__instance is not None:
			raise Exception("MemberService is a singleton, use 'MemberService.Instance()'")
		MemberService.__instance = self
	
	def get(self):
		pass
	
	def getMyCommunities(self, user):
		community = Community.objects.filter(Roles__member__User=user)
		return community
	
	def getNotJoinedCommunities(self, user):
		community = Community.objects.filter(~Q(Roles__member__User=user))
		return community
	
	def Join(self, community, user):
		model = Member()
		model.User = user
		model.Community = community
		model.save()
		roleModel = self.__roleService.GetMemberRole(community.id)
		model.Roles.add(roleModel)
		return model
	
	def AddAdminRoleToMemberModel(self, community, member):
		roleModel = self.__roleService.GetAdminRole(community.id)
		member.Roles.add(roleModel)
