import logging
from django.core.serializers import serialize

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Services.UserService import UserService
from cc.Serializers.UserSerializer import UserSerializer

class RegisterController(APIView):
	__logger = logging.getLogger('UserController')
	__userService = UserService.Instance()

	def post(self, request, format=None):
		user = self.__userService.Register(request.data)
		userSerialized = UserSerializer(user)
		return Response(userSerialized.data)