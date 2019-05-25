import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Serializers.DataTypeSerializer import DataTypeSerializer
from cc.Serializers.WorkflowSerializer import WorkflowSerializer
from cc.Services.DataTypeService import DataTypeService

from cc.Services.WorkflowService import WorkflowService


class WorkflowController(APIView):
	__logger = logging.getLogger('WorkflowController')
	__workflowService = WorkflowService.Instance()
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)

	def post(self,request, *args, **kwargs):
		id = kwargs.get('id', '')
		workflow = self.__workflowService.Create(request.data, id)
		return Response(WorkflowSerializer(workflow).data)

	def put(self,request,*args,**kwargs):
		id=kwargs.get('id','')
		workflow=self.__workflowService.Update(request.data, id)
		return Response(workflow)

	def get(self, *args, **kwargs):
		id = kwargs.get("id", "")
		workflow = self.__workflowService.Detail(id)
		return Response(WorkflowSerializer(workflow).data)


class CommunityWorkflowController(APIView):
	__logger = logging.getLogger('CommunityWorkflowController')
	__workflowService = WorkflowService.Instance()
	
	def get(self, *args, **kwargs):
		id = kwargs.get("id", "")
		list = self.__workflowService.GetByCommunity(id)
		workflowSerializer = WorkflowSerializer(list, many=True)
		return Response(workflowSerializer.data)


class CommunityDataTypeController(APIView):
	__logger = logging.getLogger('CommunityDataTypeController')
	__dataTypeService = DataTypeService.Instance()
	
	def get(self, *args, **kwargs):
		id = kwargs.get("id", "")
		list = self.__dataTypeService.GetByCommunity(id)
		dataTypeSerializer = DataTypeSerializer(list, many=True)
		return Response(dataTypeSerializer.data)
