import logging

from rest_framework.response import Response
from rest_framework.views import APIView


class ServiceController(APIView):
	__logger = logging.getLogger('ServiceController')

	def get(self, request, format=None):
		self.__logger.info('Returning "pong" response to coming ping request')
		return Response("pong")
