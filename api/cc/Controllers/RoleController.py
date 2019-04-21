import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from cc.Services.RoleService import RoleService


class RoleController(APIView):
	__logger = logging.getLogger('RoleController')
	__roleService = RoleService.Instance()