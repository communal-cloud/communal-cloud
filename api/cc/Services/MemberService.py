import logging

from cc.models import Execution, Task, ExecutionData, DataField, DataType, TaskType


class MemberService(object):
	__instance = None
	__logger = logging.getLogger('MemberService')
	
	@staticmethod
	def Instance():
		if MemberService.__instance is None:
			MemberService()
		return MemberService.__instance
	
	def __init__(self):
		if MemberService.__instance is not None:
			raise Exception("MemberService is a singleton, use 'MemberService.Instance()'")
		MemberService.__instance = self
	
	def Join(self, community, user):
		model= Member()
	