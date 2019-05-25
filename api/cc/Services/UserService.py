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
		registerSerializer = RegisterSerializer(data = userData)
		registerSerializer.is_valid(raise_exception=True)
		user = CreateNewUser(registerSerializer.data)
		SendActivationEmail(user)
		return user
	
	def UpdateUser(self, user, updateData):
		if ('email' in updateData):
			user.email = updateData['email']
		if ('name' in updateData): 
			user.name = updateData['name']
		if ('password' in updateData):
			user.password = updateData['password']
		user.clean_fields()
		user.set_password(user.password)
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

	def ForgotPassword(self, email):
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


def CreateNewUser(userData):
	user = User(
		name = userData['name'],
		email = userData['email'],
		password = userData['password'],
		is_superuser = False,
		is_staff = False,
		is_active = False
	)
	user.set_password(user.password)
	user.save()

	return user

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
	+ "Email: " + user.email + "\n" \
	+ "Password: " + newPassword
	emailFrom = "noreply@communalcloud.net"
	emailTo = (user.email,)
	send_mail(subject, message, emailFrom, emailTo)

def GenerateAndSaveNewPassword(user):
	passwordLength = 10
	mustIncludeList = ["-*'#$%_&()[]{}=+/!^", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
	totalCharList = ''.join(mustIncludeList) + "0123456789"

	newPassword = random_string_generator(size = passwordLength, chars = totalCharList)
	newPasswordToList = list(newPassword)
	passwordIndexList = list(range(0, passwordLength))
	mustIncludeIndexList = random.sample(passwordIndexList, len(mustIncludeList))
	for mustIncludeCharlist in mustIncludeList:
		indexToChange = int(mustIncludeIndexList[0])
		newPasswordToList[indexToChange] = random.choice(mustIncludeCharlist)
		mustIncludeIndexList.pop(0)
	newPassword = ''.join(newPasswordToList)
	
	user.set_password(newPassword)
	user.save()
	return newPassword

def random_string_generator(size=50, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))