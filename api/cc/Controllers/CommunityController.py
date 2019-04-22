import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from cc.Services.CommunityService import CommunityService


class CommunityController(APIView):
    __logger = logging.getLogger('CommunityController')
    __communityService = CommunityService.Instance()

    def post(self, request, format=None):
        self.__communityService.Create(request.data)
        result = None
        return Response(result)
