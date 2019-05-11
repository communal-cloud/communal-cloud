import logging

from cc.models import Task


class TaskService(object):
	__instance = None
	__logger = logging.getLogger('TaskService')
	
	@staticmethod
	def Instance():
		if TaskService.__instance is None:
			TaskService()
		return TaskService.__instance
	
	def __init__(self):
		if TaskService.__instance is not None:
			raise Exception("TaskService is a singleton, use 'TaskService.Instance()'")
		TaskService.__instance = self
	
	def Create(self, request):
		model = Task()
		model.Name = request.get("Name", u"")
		model.Description = request.get("Description", u"")
		model.save()
