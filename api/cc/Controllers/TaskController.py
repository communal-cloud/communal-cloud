import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from cc.Serializers.TaskSerializer import TaskSerializer

from cc.Services.TaskService import TaskService


class TaskController(APIView):
	__logger = logging.getLogger('TaskController')
	__taskService = TaskService.Instance()
	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)

	def post(self, request, *args, **kwargs):
		id = kwargs.get('id', '')
		task = self.__taskService.Create(request.data, id)
		return Response(TaskSerializer(task).data)


	def put(self, request, *args, **kwargs):
		id = kwargs.get('id', '')
		task = self.__taskService.Update(request.data, id)
		return Response(TaskSerializer(task).data)

	def get(self,*args, **kwargs):
		id = kwargs.get('id', '')
		task=self.__taskService.Detail(id)
		return Response(TaskSerializer(task).data)


	def delete(self, *args, **kwargs):
		id=kwargs.get("id","")
		return self.__taskService.Delete(id)
