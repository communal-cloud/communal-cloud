import logging


class WorkflowService(object):
	__instance = None
	__logger = logging.getLogger('WorkflowService')

	@staticmethod
	def Instance():
		if WorkflowService.__instance is None:
			WorkflowService()
		return WorkflowService.__instance

	def __init__(self):
		if WorkflowService.__instance is not None:
			raise Exception("WorkflowService is a singleton, use 'WorkflowService.Instance()'")
		WorkflowService.__instance = self