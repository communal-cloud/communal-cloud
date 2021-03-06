import logging

from django.http import JsonResponse
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Serializers.CommunitySerializer import CommunitySerializer
from cc.Services.CommunityService import CommunityService
from cc.Services.MemberService import MemberService


class CommunityController(APIView):
	__logger = logging.getLogger('CommunityController')
	__communityService = CommunityService.Instance()
	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, *args, **kwargs):
		id = kwargs.get('id', '')
		model = self.__communityService.Get(id)
		return Response(CommunitySerializer(model).data)
	
	def post(self, request, format=None):
		user = request.user
		model = self.__communityService.Create(request.data, user)
		return Response(CommunitySerializer(model).data)
	
	def put(self, request, *args, **kwargs):
		id = kwargs.get('id', '')
		community = self.__communityService.Update(request.data, id)
		return Response(CommunitySerializer(community).data)
	
	def delete(self, request, *args, **kwargs):
		community_id = kwargs.get('id', '')
		self.__communityService.Delete(community_id)
		return JsonResponse({'status': 'OK'}, status=200)


class CommunityViewSetController(ViewSet):
	__logger = logging.getLogger('CommunityViewSetController')
	__communityService = CommunityService.Instance()
	__memberService = MemberService.Instance()

	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	@action(detail=True, methods=['get', 'post'])
	def search(self, request, pk=None):
		community = self.__communityService.Search(request.data)
		return Response(CommunitySerializer(community, many=True).data)
	
	@action(detail=True, methods=['get'])
	def notjoined(self, request, pk=None):
		user = request.user
		communities = self.__memberService.getNotJoinedCommunities(user)
		return Response(CommunitySerializer(communities, many=True).data)