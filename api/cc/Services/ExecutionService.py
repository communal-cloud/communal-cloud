import logging
from itertools import groupby

from django.db.models.expressions import RawSQL

from cc.Services.MemberService import MemberService
from cc.models import Execution, Task, ExecutionData, DataField, DataType, TaskType, Community, BaseModel, ClassEnum


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
	
	def groupInputs(self, x):
		if x.DataGroup == None:
			x.DataGroup = x
		return int(x.DataGroup.Value)
	
	def Get(self, taskId, filter, user):
		query = '''
SELECT d.*
FROM cc_execution e
  LEFT JOIN cc_execution_Data ed ON e.basemodel_ptr_id = ed.execution_id
  LEFT JOIN cc_executiondata d ON d.basemodel_ptr_id = ed.executiondata_id

WHERE Field_id  IN (SELECT f.datafield_id FROM cc_task t
     LEFT JOIN cc_task_InputFields f ON t.basemodel_ptr_id = f.task_id
   WHERE t.basemodel_ptr_id = %s)
ORDER BY d.DataGroup_id
'''
		
		inputs = list(ExecutionData.objects.raw(query, [taskId]))
		for f in filter:
			field = DataField.objects.get(pk=f.get("Field", None))
			value = f.get("Value", None)
			if not value and field.Type is ClassEnum.User.value:
				value = user.pk
			groups = [x.DataGroup.Value for x in inputs if x.Field_id == field.id and x.Value == value]
			inputs = [x for x in inputs if x.DataGroup.Value in groups]
		
		groupedInputs = [list(v) for k, v in groupby(inputs, key=self.groupInputs)]
		return groupedInputs
	
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
			identifier.DataGroup = identifier
			identifier.save()
			
			model.Data.add(identifier)
		group = identifier
		for field in fields:
			fieldModel = DataField.objects.get(pk=field.get("Field", None))
			if not field.get("Value", None) and fieldModel.Type is ClassEnum.User.value:
				field["Value"] = user.id
				
			ed = self.SaveExecutionData(field, model.Task, group)
			model.Data.add(ed)
			return model
	
	def SaveExecutionData(self, field, task, group=None):
		model = ExecutionData()
		model.DataGroup = group
		model.Field_id = field.get("Field", None)
		model.Value = field.get("Value", None)
		model.Task = task
		model.save()
		return model
	
	def GetIdentifierField(self, id):
		task = Task.objects.get(pk=id)
		dataField = task.OutputFields.first()
		dataType = dataField.datatype_set.first()
		identifier = dataType.Fields.filter(Name="Identifier").first()
		return identifier
