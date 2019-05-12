import logging

from cc.models import Execution, Task, ExecutionData, DataField


class ExecutionService(object):
	__instance = None
	__logger = logging.getLogger('ExecutionService')
	
	@staticmethod
	def Instance():
		if ExecutionService.__instance is None:
			ExecutionService()
		return ExecutionService.__instance
	
	def __init__(self):
		if ExecutionService.__instance is not None:
			raise Exception("ExecutionService is a singleton, use 'ExecutionService.Instance()'")
		ExecutionService.__instance = self
	
	def Save(self, execution, user):
		model = Execution()
		model.Task = Task.objects.get(pk=execution.get("Task", ""))
		model.ExecutedBy = user
		model.save()
		fields = execution.get("Data", [])
		group = None  # TODO: If fields contains "Identifier" filed take the value
		for field in fields:
			self.SaveDataField(field, group)
	
	def SaveDataField(self, field, group=None):
		model = ExecutionData()
		model.DataDataGroup = group
		model.DataField = DataField.objects.get(pk=field.get("DataField", ""))
		model.DataValue = field.get("Data", None)  # TODO: If does not work put the data in a dictionary
		model.save()
