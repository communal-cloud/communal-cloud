import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Services.CommunityService import CommunityService



class CommunityController(APIView):
    __logger = logging.getLogger('CommunityController')
    __communityService = CommunityService.Instance()
  #  authentication_classes = (TokenAuthentication,)
   # permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        self.__communityService.Create(request.data)
        result = None
        return Response(result)
    
    def put(self, request, *args, **kwargs):
        id = kwargs.get('id', 'Default Value if not there')
        self.__communityService.Update(request.data, id)
        result = None
        return Response(result)