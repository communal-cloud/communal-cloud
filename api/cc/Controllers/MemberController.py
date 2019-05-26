import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Serializers.CommunitySerializer import CommunitySerializer
from cc.Services.MemberService import MemberService
from cc.Services.UserService import UserService
from cc.Services.RoleService import RoleService
from cc.Serializers.RoleSerializer import RoleSerializer


class MemberController(APIView):
	__logger = logging.getLogger('MemberController')
	__memberService = MemberService.Instance()
	
	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self, *args, **kwargs):
		pass
	

class CommunityMemberController(APIView):
	__logger = logging.getLogger('CommunityMemberController')
	__memberService = MemberService.Instance()
	__userService = UserService.Instance()
	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, *args, **kwargs):
		user = request.user
		if user is not None:
			member_comm = self.__memberService.getMyCommunities(user)
			return Response(CommunitySerializer(member_comm, many=True).data)
		else:
			return NotFound


class RoleMemberController(APIView):
	__logger = logging.getLogger('RoleMemberController')
	__memberService = MemberService.Instance()
	__roleService = RoleService.Instance()
	
	def get(self, *args, **kwargs):
		member_id = kwargs.get('id', '')
		roles = self.__roleService.GetListByMemberId(member_id)
		return Response(RoleSerializer(roles, many=True).data)
	
