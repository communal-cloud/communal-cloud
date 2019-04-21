import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from cc.Services.CategoryService import CategoryService


class CategoryController(APIView):
	__logger = logging.getLogger('CategoryController')
	__categoryService = CategoryService.Instance()