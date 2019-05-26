import logging

from cc.Services.MemberService import MemberService
from cc.models import Execution, Task, ExecutionData, DataField, DataType, TaskType, Community, BaseModel


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
		query='''SELECT d.*
				FROM cc_execution e
				  LEFT JOIN cc_execution_Data ed ON e.basemodel_ptr_id = ed.execution_id
				  LEFT JOIN cc_executiondata d ON d.basemodel_ptr_id = ed.executiondata_id
				
				WHERE Field_id IN (SELECT f.datafield_id
                   FROM cc_task t
                     LEFT JOIN cc_task_InputFields f ON t.basemodel_ptr_id = f.task_id
                   WHERE t.basemodel_ptr_id =%s)
'''
		inputs=ExecutionData.objects.raw(query,[id])
		return inputs
	
	def Save(self, execution, user):
		model = Execution()
		model.Task = Task.objects.get(pk=execution.get("Task", ""))
		if model.Task.Type == TaskType.Join.value:
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
			newIdx = BaseModel.objects.last().id
			if lastExecution:
				newIdx = lastExecution.id
			
			identifier = ExecutionData.objects.create(Field=identifierField, Value=newIdx)
			model.Data.add(identifier)
		group = identifier
		for field in fields:
			ed = self.SaveExecutionData(field, group)
			model.Data.add(ed)
	
	def SaveExecutionData(self, field, group=None):
		model = ExecutionData()
		model.DataGroup = group
		model.Field_id = field.get("Field", None)
		model.Value = field.get("Value", None)
		model.save()
		return model
	
	def GetIdentifierField(self, id):
		task = Task.objects.get(pk=id)
		dataField = task.OutputFields.first()
		dataType = dataField.datatype_set.first()
		identifier = dataType.Fields.filter(Name="Identifier").first()
		return identifier
