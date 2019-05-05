import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json

from cc.Services.DataService import DataService


class FieldClassController(APIView):
	__logger = logging.getLogger('DataController')
	__dataService = DataService.Instance()
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)

	def get(self,request):
		enum= self.__dataService.getEnum()
		return Response(enum)

	def post(self,request):
		datatype=self.__dataService.createDataType(request.data)
		for field in request.data.get("Fields",u""):
			self.__dataService.createDataField(field,datatype)


