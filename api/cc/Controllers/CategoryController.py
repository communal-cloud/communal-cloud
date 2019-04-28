import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Services.CategoryService import CategoryService


class CategoryController(APIView):
	__logger = logging.getLogger('CategoryController')
	__categoryService = CategoryService.Instance()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def post(self, request, format=None):
		self.__categoryService.Create(request.data)
		result = None
		return Response(result)