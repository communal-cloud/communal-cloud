import logging

from django.http import JsonResponse
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
import json

from cc.Serializers.DataTypeSerializer import DataTypeSerializer
from cc.Services.DataService import DataService


class FieldClassController(APIView):
	__logger = logging.getLogger('DataController')
	__dataService = DataService.Instance()
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)

	def get(self,request):
		enum= self.__dataService.getEnum()
		return Response(enum)

	def post(self,request, *args, **kwargs):
		id = kwargs.get('id', '')
		datatype=self.__dataService.createDataType(request.data, id)
		for field in request.data.get("Fields",u""):
			self.__dataService.createDataField(field,datatype)
		response = Response(DataTypeSerializer(datatype).data)
		
		return response

	def put (self, request, *args, **kwargs):
		dataTypeId = kwargs.get('id', '')
		datatype = self.__dataService.updateDataType(dataTypeId, request.data)
		currentDataFieldList = datatype.Fields.all()
		dataFieldListToUpdate = request.data.get("Fields",u"")
		self.__dataService.updateDataFields(datatype, currentDataFieldList, dataFieldListToUpdate)
		return Response(DataTypeSerializer(datatype).data)
		