import logging
from django.core.serializers import serialize

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from cc.Services.UserService import UserService
from cc.Serializers.UserSerializer import UserSerializer
from cc.models import User


class UserController(ViewSet):
	__logger = logging.getLogger('UserController')
	__userService = UserService.Instance()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	@action(detail=True, methods=['get'])
	def get(self, request, pk=None):
		user = request.user
		userJson = UserSerializer(user)

		return Response(userJson.data)

	@action(detail=True, methods=['get'])
	def logout(self, request, pk=None):
		return self.__userService.Logout(request.user)
