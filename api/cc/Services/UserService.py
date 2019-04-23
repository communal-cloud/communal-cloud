import logging
from django.http import JsonResponse

from cc.Serializers.RegisterSerializer import RegisterSerializer
from rest_framework.authtoken.models import Token

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
	
	def Register(self, userData):
		registerSerializer = RegisterSerializer(data = userData)
		registerSerializer.is_valid()
		user = registerSerializer.create(registerSerializer.data)
		user.is_active = True
		user.set_password(user.password)
		user.save()
		return user
	
	def ActivateEmail(self, code):
		raise NotImplementedError
	
	def Logout(self, userData):
		token = Token(key = userData.auth_token.key)
		token.delete()
		return JsonResponse({'status':'OK' }, status=200)
