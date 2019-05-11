import logging
import string
import random
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail

from cc.Serializers.RegisterSerializer import RegisterSerializer
from rest_framework.authtoken.models import Token
from cc.models import ActivationToken, User

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
		userData["groups"] = []
		userData["user_permissions"] = []
		registerSerializer = RegisterSerializer(data = userData)
		registerSerializer.is_valid()
		user = registerSerializer.create(registerSerializer.data)
		user.set_password(user.password)
		user.save()
		SendActivationEmail(user)
		return user
	
	def UpdateUser(self, user, updateData):
		if ('username' in updateData):
			user.username = updateData['username']
		if ('name' in updateData): 
			user.name = updateData['name']
		if ('password' in updateData):
			user.set_password(updateData['password'])
		user.save()
		return user
	
	def DeleteUser(self, user):
		user.delete()
		return JsonResponse({'status':'OK' }, status=200)

	def ActivateEmail(self, token):
		activationTokenRegistry = ActivationToken.objects.get(token = token)
		user = User.objects.get(id = activationTokenRegistry.userId)
		user.is_active = True
		user.save()
		activationTokenRegistry.delete()
		return JsonResponse({'status':'OK' }, status=200)

	def ForgotPassword(self, email, baseUrl):
		try:
			user = User.objects.get(email = email)
		except:
			return JsonResponse({'status':'There is no user registered with that email address'}, status=422 )
		SendForgotPasswordEmail(user)
		return JsonResponse({'status':'OK' }, status=200)
	
	def Logout(self, userData):
		token = Token(key = userData.auth_token.key)
		token.delete()
		return JsonResponse({'status':'OK' }, status=200)

def SendActivationEmail(user):
	baseUrl = settings.BASE_URL
	token = GenerateAndSaveActivationToken(user.id)
	activationLink = baseUrl + "user/activation/" + token
	subject = "Communal-Cloud Activation"
	message = "Please activate your email to login by clicking the link below.\n\n" + activationLink
	emailFrom = "noreply@communalcloud.net"
	emailTo = (user.email,)
	send_mail(subject, message, emailFrom, emailTo)

def GenerateAndSaveActivationToken(userId):
	token = random_string_generator()
	recordWithSameToken = ActivationToken(token = token)
	recordWithSameUserId = ActivationToken(userId = userId)
	if (recordWithSameToken.pk != None):
		GenerateAndSaveActivationToken(userId)
	elif (recordWithSameUserId.pk != None):
		recordWithSameUserId.delete()
	else:
		newRecord = ActivationToken(
			token = token,
			userId = userId,
		)
		newRecord.save()
		return token

def SendForgotPasswordEmail(user):
	newPassword = GenerateAndSaveNewPassword(user)
	subject = "Communal-Cloud Password Change"
	message = "Your user credentials are below.\n\n" \
	+ "Username: " + user.username + "\n" \
	+ "Password: " + newPassword
	emailFrom = "noreply@communalcloud.net"
	emailTo = (user.email,)
	send_mail(subject, message, emailFrom, emailTo)

def GenerateAndSaveNewPassword(user):
	newPassword = random_string_generator(size = 10)
	user.set_password(newPassword)
	user.save()
	return newPassword

def random_string_generator(size=50, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))