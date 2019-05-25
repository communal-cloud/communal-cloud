import logging

from django.http import JsonResponse

from cc.models import Task, Workflow, User, Role, DataField, TaskType


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
	
	def Create(self, request, id):  # id is workflows pk.
		workflow = Workflow.objects.get(pk=id)
		model = Task()
		model.Workflow_id = workflow.pk
		model.Name = request.get("Name", u"")
		model.Description = request.get("Description", u"")
		model.Available = request.get("Available", u"")
		model.AvailableTill = request.get("AvailableTill", u"")
		model.AvailableTimes = request.get("AvailableTimes", u"")
		if "Type" in request:
			model.Type=request.get("Type", u"")
		else:
			model.Type=TaskType.Execution.value
		model.save()
		if "AssignedUsers" in request:
			for user_id in request.get("AssignedUsers", []):
				user = User.objects.get(pk=user_id)
				model.AssignedUsers.add(user)
		if "AssignedRoles" in request:
			for role_id in request.get("AssignedRoles", []):
				role = Role.objects.get(pk=role_id)
				model.AssignedRoles.add(role)
		if "Predecessors" in request:
			for task_id in request.get("Predecessors", []):
				prod = Task.objects.get(pk=task_id)
				model.Predecessors.add(prod)
		if "InputFields" in request:
			for input_datafield_id in request.get("InputFields", []):
				input_field = DataField.objects.get(pk=input_datafield_id)
				model.InputFields.add(input_field)
		if "OutputFields" in request:
			for output_datafield_id in request.get("OutputFields", []):
				output_field = DataField.objects.get(pk=output_datafield_id)
				model.OutputFields.add(output_field)
		return model

	def Update(self, request, id):  # id is workflows pk.
		model = Task.objects.get(pk=id)
		model.Name = request.get("Name", u"")
		model.Description = request.get("Description", u"")
		model.Available = request.get("Available", u"")
		model.AvailableTill = request.get("AvailableTill", u"")
		model.AvailableTimes = request.get("AvailableTimes", u"")
		model.save()
		model.AssignedUsers.clear()
		if "AssignedUsers" in request.data:
			for user_id in request.get("AssignedUsers", []):
				user = User.objects.get(pk=user_id)
				model.AssignedUsers.add(user)
		model.AssignedRoles.clear()
		if "AssignedRoles" in request.data:
			for role_id in request.get("AssignedRoles", []):
				role = Role.objects.get(pk=role_id)
				model.AssignedRoles.add(role)
		model.Predecessors.clear()
		if "Predecessors" in request.data:
			for task_id in request.get("Predecessors", []):
				prod = Task.objects.get(pk=task_id)
				model.Predecessors.add(prod)
		model.InputFields.clear()
		if "InputFields" in request.data:
			for input_datafield_id in request.get("InputFields", []):
				input_field = DataField.objects.get(pk=input_datafield_id)
				model.InputFields.add(input_field)
		model.OutputFields.clear()
		if "OutputFields" in request.data:
			for output_datafield_id in request.get("OutputFields", []):
				output_field = DataField.objects.get(pk=output_datafield_id)
				model.OutputFields.add(output_field)
		return model

	def Detail(self, id):
		return Task.objects.get(pk=id)

	def GetList(self, id):
		workflow=Workflow.objects.get(pk=id)
		taskList=Task.objects.filter(Workflow=workflow)
		return taskList

	def Delete(self, id):
		task=Task.objects.get(pk=id)
		task.delete()
		return JsonResponse({'status':'OK' }, status=200)
