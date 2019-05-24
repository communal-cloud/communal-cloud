import logging

from pycodestyle import ambiguous_identifier

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
		indentifier = fields.filter(lambda f: f.Field.Name == "Identifier")
		if not indentifier:
			identifierField = self.GetIdentifierField(model.Task.id)
			identifier = ExecutionData.save(DataField=identifierField, Value=ExecutionData.objects.latest.id + 1)
		group = identifier
		for field in fields:
			self.SaveExecutionData(field, group)
	
	def SaveExecutionData(self, field, group=None):
		model = ExecutionData()
		model.DataGroup = group
		model.Field = DataField.objects.get(pk=field.get("DataField", ""))
		model.Value = field.get("Data", None)  # TODO: If does not work put the data in a dictionary
		model.save()
	
	def GetIdentifierField(self, id):
		return
