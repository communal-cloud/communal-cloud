import logging


class UserService(object):
	__instance = None
	__logger = logging.getLogger('UserService')

	@staticmethod
	def Instance():
		if UserService.__instance is None:
			UserService()
		return UserService.__instance

	def __init__(self):
		if UserService.__instance is not None:
			raise Exception("UserService is a singleton, use 'UserService.Instance()'")
		UserService.__instance = self