import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from cc.Services.UserService import UserService


class UserController(APIView):
	__logger = logging.getLogger('UserController')
	__userService = UserService.Instance()
	
	def get(self, request, format=None):
		id = request.query_params.get("id", None)
		result = None
		return Response(result)
