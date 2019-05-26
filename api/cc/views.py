import logging

from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from cc.Serializers.TaskSerializer import TaskSerializer
from cc.Serializers.RoleSerializer import RoleSerializer
from cc.Serializers.CommunitySerializer import CommunitySerializer
from cc.Serializers.MemberSerializer import MemberSerializer

from cc.Services.TaskService import TaskService
from cc.Services.RoleService import RoleService
from cc.Services.CommunityService import CommunityService

from cc.models import Task
from cc.models import Role


class TasksController(APIView):
    __logger = logging.getLogger('TaskController')
    __taskService = TaskService.Instance()
    queryset=Task.objects.all()

    def get(self, *args, **kwargs):
        id=kwargs.get("id","")
        taskList=self.__taskService.GetList(id)
        return Response(TaskSerializer(taskList, many=True).data)


class RolesController(APIView):
    __logger = logging.getLogger('RolesController')
    __role_service = RoleService.Instance()
    
    def get(self, *args, **kwargs):
        community_id = kwargs.get('id', '')
        roles = self.__role_service.GetList(community_id)
        return Response(RoleSerializer(roles, many=True).data)
    

class AllCommunitiesController(APIView):
    __logger = logging.getLogger('AllCommunitiesController')
    __community_service = CommunityService.Instance()
    
    def get(self, *args, **kwargs):
        communities = self.__community_service.GetList()
        return Response(CommunitySerializer(communities, many=True).data)
    

class AllActiveCommunitiesController(APIView):
    __logger = logging.getLogger('AllActiveCommunitiesController')
    __community_service = CommunityService.Instance()
    
    def get(self, *args, **kwargs):
        active_communities = self.__community_service.GetActiveList()
        return Response(CommunitySerializer(active_communities, many=True).data)

class MembersOfCommunityController(APIView):
    __logger = logging.getLogger('AllActiveCommunitiesController')
    __community_service = CommunityService.Instance()

    #  authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
    
    def get(self, *args, **kwargs):
        communityId = kwargs.get('id', '')
        members = self.__community_service.getMembersOfCommunity(communityId)
        return Response(MemberSerializer(members, many=True).data)
    