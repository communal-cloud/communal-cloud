import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from cc.Services.TaskService import TaskService


class TaskController(APIView):
	__logger = logging.getLogger('TaskController')
	__taskService = TaskService.Instance()