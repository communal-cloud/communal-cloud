import logging

from django.db.migrations.serializer import DictionarySerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Serializers.ExecutionDataSerializer import ExecutionDataSerializer, GroupedExecutionDataSerializer
from cc.Serializers.ExecutionSerializer import ExecutionSerializer
from cc.Services.ExecutionService import ExecutionService
from cc.models import Execution


class ExecutionController(APIView):
	__logger = logging.getLogger('ExecutionController')
	__executionService = ExecutionService.Instance()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, *args, **kwargs):
		id = kwargs.get("id", "")
		response = self.__executionService.Get(request.user, id)
		return Response(ExecutionDataSerializer(response, many=True).data)
	
	def post(self, request, format=None):
		response = self.__executionService.Save(request.data, request.user)
		return Response(ExecutionSerializer(response).data)

	def put(self, request, *args, **kwargs):
		id = kwargs.get("id", "")
		execution=Execution.objects.get(pk=id)
		response = self.__executionService.Update(request.data, execution, request.user)
		return Response(ExecutionSerializer(response).data)


class ExecutionDataController(APIView):
	__logger = logging.getLogger('ExecutionDataController')
	__executionService = ExecutionService.Instance()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def post(self, request, *args, **kwargs):
		id = kwargs.get("id", "")
		response = self.__executionService.Get(id, request.data, request.user)
		return Response(GroupedExecutionDataSerializer(response).data.get("Items"))

