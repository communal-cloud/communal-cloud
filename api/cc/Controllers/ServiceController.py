import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ServiceController(APIView):
	__logger = logging.getLogger('ServiceController')
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		self.__logger.info('Returning "pong" response to coming ping request')
		return Response("pong")
