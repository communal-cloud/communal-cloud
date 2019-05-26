import logging

from cc.Services.MemberService import MemberService
from cc.models import Execution, Task, ExecutionData, DataField, DataType, TaskType, Community


class ExecutionService(object):
	__instance = None
	__logger = logging.getLogger('ExecutionService')
	__memberService = MemberService.Instance()
	
	@staticmethod
	def Instance():
		if ExecutionService.__instance is None:
			ExecutionService()
		return ExecutionService.__instance
	
	def __init__(self):
		if ExecutionService.__instance is not None:
			raise Exception("ExecutionService is a singleton, use 'ExecutionService.Instance()'")
		ExecutionService.__instance = self
	
	def Get(self, user, id):
		task=Task.objects.get(pk=id)
		task.InputFields
	
	def Save(self, execution, user):
		model = Execution()
		model.Task = Task.objects.get(pk=execution.get("Task", ""))
		if Task.Type == TaskType.Join:
			community = model.Task.Workflow.Community
			self.__memberService.Join(community, user)
		model.ExecutedBy = user
		model.save()
		fields = execution.get("Data", [])
		dataFields = DataField.objects.filter(pk__in=[i.get("Field") for i in fields])
		
		indentifier = dataFields.filter(Name="Identifier").first()
		if not indentifier:
			identifierField = self.GetIdentifierField(model.Task.id)
			lastExecution = ExecutionData.objects.last()
			newIdx = 1
			if lastExecution:
				newIdx = lastExecution.id + 1
			
			identifier = ExecutionData.objects.create(Field=identifierField, Value=newIdx)
		group = identifier
		for field in fields:
			self.SaveExecutionData(field, group)
	
	def SaveExecutionData(self, field, group=None):
		model = ExecutionData()
		model.DataGroup = group
		model.Field = DataField.objects.get(pk=field.get("Field", None))
		model.Value = field.get("Value", None)
		model.save()
	
	def GetIdentifierField(self, id):
		task = Task.objects.get(pk=id)
		dataField = task.OutputFields.first()
		dataType = dataField.datatype_set.first()
		identifier = dataType.Fields.filter(Name="Identifier").first()
		return identifier
