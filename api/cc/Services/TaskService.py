import logging

from cc.models import Task, Community, Workflow, User, Role, DataField


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
		model.Name = request.data.get("Name", u"")
		model.Description = request.data.get("Description", u"")
		model.Available = request.data.get("Available", u"")
		model.AvailableTill = request.data.get("AvailableTill", u"")
		model.AvailableTimes = request.data.get("AvailableTimes", u"")
		model.save()
		if "AssignedUsers" in request.data:
			for user_id in request.data.get("AssignedUsers", []):
				user = User.objects.get(pk=user_id)
				model.AssignedUsers.add(user)
		if "AssignedRoles" in request.data:
			for role_id in request.data.get("AssignedRoles", []):
				role = Role.objects.get(pk=role_id)
				model.AssignedRoles.add(role)
		if "Predecessors" in request.data:
			for task_id in request.data.get("Predecessors", []):
				prod = Task.objects.get(pk=task_id)
				model.Predecessors.add(prod)
		if "InputFields" in request.data:
			for input_datafield_id in request.data.get("InputFields", []):
				input_field = DataField.objects.get(pk=input_datafield_id)
				model.InputFields.add(input_field)
		if "OutputFields" in request.data:
			for output_datafield_id in request.data.get("OutputFields", []):
				output_field = DataField.objects.get(pk=output_datafield_id)
				model.OutputFields.add(output_field)
		return model