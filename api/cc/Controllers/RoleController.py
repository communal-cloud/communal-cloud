import logging

from django.http import JsonResponse
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from cc.Serializers.RoleSerializer import RoleSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Services.RoleService import RoleService


class RoleController(APIView):
	__logger = logging.getLogger('RoleController')
	__roleService = RoleService.Instance()
	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
	
	# Url'den gelen role/id'deki id, community_id'yi temsil etmekte.
	def post(self, request, *args, **kwargs):
		community_id = kwargs.get('id', '')
		self.__roleService.Create(request.data.get("Name", u""), community_id)
		return JsonResponse({'status': 'OK'}, status=200)

	def put(self, request, *args, **kwargs):
		id = kwargs.get('id', '')
		self.__roleService.Update(request.data, id)
		return JsonResponse({'status': 'OK'}, status=200)
	
	def get(self, request, *args, **kwargs):
		id = kwargs.get('id', '')
		model = self.__roleService.Get(id)
		return Response(RoleSerializer(model).data)
	
	def delete(self, request, *args, **kwargs):
		role_id = kwargs.get('id', '')
		return self.__roleService.Delete(role_id)
