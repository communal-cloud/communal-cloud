import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from cc.Serializers.TaskSerializer import TaskSerializer

from cc.Services.TaskService import TaskService
from cc.models import Task


class TasksController(APIView):
    __logger = logging.getLogger('TaskController')
    __taskService = TaskService.Instance()
    queryset=Task.objects.all()

    def get(self, *args, **kwargs):
        id=kwargs.get("id","")
        taskList=self.__taskService.GetList(id)
        return Response(TaskSerializer(taskList, many=True).data)