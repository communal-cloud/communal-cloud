import logging

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Serializers.ExecutionSerializer import ExecutionSerializer
from cc.Services.ExecutionService import ExecutionService


class ExecutionController(APIView):
	__logger = logging.getLogger('ExecutionController')
	__executionService = ExecutionService.Instance()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, *args, **kwargs):
		id=kwargs.get("id","")
		response = self.__executionService.Get(request.user, id)
		return Response(ExecutionSerializer(response).data)
		
		
	def post(self, request, format=None):
		self.__executionService.Save(request.data, request.user)
		return JsonResponse({'status': 'OK'}, status=200)