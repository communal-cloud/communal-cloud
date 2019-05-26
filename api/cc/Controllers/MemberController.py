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
from cc.Serializers.MemberSerializer import MemberSerializer


class MemberController(APIView):
	__logger = logging.getLogger('MemberController')
	__memberService = MemberService.Instance()
	
	
	#  authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
	
	def get(self, *args, **kwargs):
		pass
	

class CommunityMemberController(APIView):
	__logger = logging.getLogger('MemberViewSetController')
	__memberService = MemberService.Instance()
	__userService = UserService.Instance()
	
	def get(self, request, *args, **kwargs):
		user = request.user
		if user is not None:
			member_comm = self.__memberService.getMyCommunities(user)
			return Response(CommunitySerializer(member_comm, many=True).data)
		else:
			return NotFound
