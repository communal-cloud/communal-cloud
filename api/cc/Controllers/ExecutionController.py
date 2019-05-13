import logging

from django.http import JsonResponse
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Services.ExecutionService import ExecutionService


class ExecutionController(APIView):
	__logger = logging.getLogger('ExecutionController')
	__executionService = ExecutionService.Instance()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def post(self, request, format=None):
		self.__executionService.Save(request.data, request.user)
		return JsonResponse({'status': 'OK'}, status=200)