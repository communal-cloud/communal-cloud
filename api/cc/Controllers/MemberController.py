import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Serializers.CommunitySerializer import CommunitySerializer
from cc.Services.CommunityService import CommunityService


class MemberController(APIView):
	__logger = logging.getLogger('MemberController')
	__communityService = CommunityService.Instance()
	
	#  authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
	