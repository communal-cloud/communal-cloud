import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from api.cc.Services.ExecutionService import ExecutionService


class ExecutionController(APIView):
	__logger = logging.getLogger('ExecutionController')
	__executionService = ExecutionService.Instance()