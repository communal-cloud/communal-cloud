import logging

from cc.Services.CategoryService import CategoryService
from cc.Services.DataService import DataService
from cc.Services.RoleService import RoleService
from cc.Services.TaskService import TaskService
from cc.Services.WorkflowService import WorkflowService
from cc.models import Community, ClassEnum, Category, TaskType, RoleType, Member
from cc.Services.MemberService import MemberService


class CommunityService(object):
	__instance = None
	__logger = logging.getLogger('CommunityService')
	__categoryService = CategoryService.Instance()
	__dataService = DataService.Instance()
	__roleService = RoleService.Instance()
	__taskService = TaskService.Instance()
	__workflowService = WorkflowService.Instance()
	__memberService = MemberService.Instance()
	
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
		model = Community.objects.get(pk=id)
		return model
	
	def GetRecent(self, count):
		raise NotImplementedError
	
	def GetPopular(self, count):
		raise NotImplementedError
	
	def Create(self, community, user):
		model = Community()
		if "Name" in community:
			model.Name = community.get("Name", u"")
		else:
			raise Exception("Name is required!")
		if "Description" in community:
			model.Description = community.get("Description", u"")
		
		if "Purpose" in community:
			model.Purpose = community.get("Purpose", u"")
		model.save()
		if "Categories" in community:
			for c in community.get("Categories", u""):
				obj, created = self.__categoryService.GetOrCreate(c)
				model.Categories.add(obj)
		if "Roles" in community:
			for r in community.get("Roles", u""):
				obj, created = self.__roleService.GetOrCreate(r)
				model.Roles.add(obj)
		userDataType = self.__createDefaultMemberDataType(model.pk)
		self.__createDefaultRoles(model.pk)
		self.__createDefaultJoinTask(model.pk, userDataType)
		memberModel = self.__memberService.CreateAdminMember(model, user)
		self.__memberService.AddAdminRoleToMemberModel(model, memberModel)
		return model
	
	def Update(self, community, id):
		model = Community.objects.get(pk=id)
		if "Name" in community:
			model.Name = community.get("Name", u"")
		# TODO: name can be changed if number of member of the group has less than n members.
		if "Description" in community:
			model.Description = community.get("Description", u"")
		
		if "Purpose" in community:
			model.Purpose = community.get("Purpose", u"")
		model.save()
		model.Categories.clear()
		if "Categories" in community:
			for c in community.get("Categories", u""):
				obj, created = self.__categoryService.GetOrCreate(c)
				model.Categories.add(obj)
		
		if "Roles" in community:
			for r in community.get("Roles", u""):
				obj, created = self.__roleService.GetOrCreate(r)
				model.Roles.add(obj)
		return model
	
	def Activate(self, community):
		raise NotImplementedError
	
	def Delete(self, id):
		model = Community.objects.get(pk=id)
		model.delete()
	
	def GetList(self):
		return Community.objects.all()
	
	def GetActiveList(self):
		return Community.objects.filter(Deleted=0)
	
	def Search(self, searchRequest):
		if "Name" in searchRequest:
			searchContext = searchRequest.get("Name", u"")
			return Community.objects.filter(Name__icontains=searchContext)
		elif "Purpose" in searchRequest:
			searchContext = searchRequest.get("Purpose", u"")
			return Community.objects.filter(Purpose__icontains=searchContext)
		elif "Category" in searchRequest:
			searchContext = searchRequest.get("Category", u"")
			category = Category.objects.filter(Name__icontains=searchContext).values_list('id', flat=True)
			categoryIdList = list(category)
			communityList = Community.objects.filter(Categories__in=categoryIdList)
			communityList.query.group_by = ["id"]
			return communityList
	
	def __createDefaultRoles(self, pk):
		self.__roleService.Create("Member", pk, RoleType.Member.value)
		self.__roleService.Create("Admin", pk, RoleType.Admin.value)
	
	def getMembersOfCommunity(self, communityId):
		members = Member.objects.filter(Roles__community__id=communityId).all()
		return members
	
	def __createDefaultMemberDataType(self, id):
		data = {
			"Name": "Member",
			"Fields": [
				{
					"Name": "User",
					"Class": ClassEnum.User.value
				}
			]
		}
		
		dataType = self.__dataService.createDataType(data, id)
		for field in data.get("Fields", []):
			self.__dataService.createDataField(field, dataType)
		
		return dataType
	
	def __createDefaultJoinWorkflow(self, pk):
		data = {
			"Name": "Membership Workflow",
			"Description": "This contains the tasks for member operations"
		}
		workflow = self.__workflowService.Create(data, pk)
		return workflow
	
	def __createDefaultJoinTask(self, pk, user):
		workflow_id = self.__createDefaultJoinWorkflow(pk).pk
		TaskData = {
			"Name": "Join",
			"Description": "This is the task that every member of the system will have to follow in order to join the Community",
			"Available": True,
			"AvailableTill": None,
			"AvailableTimes": 10000,
			"InputField": user.pk,
			"Type": TaskType.Join.value
		}
		self.__taskService.Create(TaskData, workflow_id)
