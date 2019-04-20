import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from api.cc.Services.CommunityService import CommunityService


class CommunityController(APIView):
	__logger = logging.getLogger('CommunityController')
	__communityService = CommunityService.Instance()