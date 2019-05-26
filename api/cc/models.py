import datetime
from enum import Enum

from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.utils import timezone
from jsonfield import JSONField

from cc.UserManager import UserManager


class ClassEnum(Enum):
	NotSpecified = 0
	Integer = 1
	String = 2
	Boolean = 3
	DateTime = 4
	GeoLocation = 5
	Relation = 6
	User = 7
	Image = 8


class TaskType(Enum):
	NotSpecified = 0
	Execution = 1
	Join = 2
	Leave = 3


class BaseManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(Deleted=False)


class BaseModel(models.Model):
	CreatedOn = models.DateTimeField(editable=False)
	ModifiedOn = models.DateTimeField(editable=False)
	Deleted = models.BooleanField(default=False)
	
	objects = BaseManager()
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.CreatedOn = timezone.now()
		else:
			del self.CreatedOn
		self.ModifiedOn = timezone.now()
		return super(BaseModel, self).save(*args, **kwargs)
	
	def delete(self, *args, **kwargs):
		self.Deleted = True
		self.save()


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=100)
	is_superuser = models.BooleanField(null=True)
	is_active = models.BooleanField(null=True)
	is_staff = models.BooleanField(null=True)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']
	
	objects = UserManager()


class ActivationToken(models.Model):
	token = models.CharField(max_length=50, unique=True, null=False)
	userId = models.IntegerField(unique=True, null=False)
	
	objects = models.Manager()


class Role(BaseModel):
	Name = models.CharField(max_length=50)
	SystemDefined = models.BooleanField(default=True)
	
	def __str__(self):
		return u'Role {0} ({1})'.format(self.Name, self.id)
	
	def __unicode__(self):
		return u'Role {0} ({1})'.format(self.Name, self.id)


class Category(BaseModel):
	Name = models.CharField(max_length=100)
	
	def __str__(self):
		return u'Category {0} ({1})'.format(self.Name, self.id)
	
	def __unicode__(self):
		return u'Category {0} ({1})'.format(self.Name, self.id)


class DataEnumeration(BaseModel):
	Name = models.CharField(max_length=50)
	Value = JSONField(default="{}")
	
	def __str__(self):
		return u'DataEnumeration {0} ({1})'.format(self.Name, self.id)
	
	def __unicode__(self):
		return u'DataEnumeration {0} ({1})'.format(self.Name, self.id)


class DataField(BaseModel):
	Name = models.CharField(max_length=50)
	Type = models.IntegerField(choices=[(choice.value, choice.name.replace("_", " ")) for choice in ClassEnum])
	Enumerations = models.ManyToManyField(DataEnumeration, blank=True)
	Parameters = JSONField(default="{}")
	Saved = models.BooleanField(default=False)
	
	@property
	def Class(self):
		from cc.Services.ClassImplementations import FieldClass
		return FieldClass().Get(self.Type)
	
	def __str__(self):
		typeName = ClassEnum(int(self.Type)).name.replace('_', ' ')
		return u'{0} DataField {1} ({2})'.format(typeName, self.Name, self.id)
	
	def __unicode__(self):
		typeName = ClassEnum(int(self.Type)).name.replace('_', ' ')
		return u'{0} DataField {1} ({2})'.format(typeName, self.Name, self.id)


class Community(BaseModel):
	Name = models.CharField(max_length=50)
	Purpose = models.CharField(max_length=250, blank=True, null=True)
	Description = models.CharField(max_length=5000, blank=True, null=True)
	Roles = models.ManyToManyField(Role, blank=True)
	Categories = models.ManyToManyField(Category, related_name="Categories", blank=True)
	IsCompleted = models.BooleanField(default=False)
	
	def __str__(self):
		return u'Community {0} ({1})'.format(self.Name, self.id)
	
	def __unicode__(self):
		return u'Community {0} ({1})'.format(self.Name, self.id)
	
	@property
	def isMember(self, user):
		membership = Member.objects.filter(Community=self, User=user)
		if membership:
			return True
		return False


class Workflow(BaseModel):
	Name = models.CharField(max_length=50)
	Description = models.CharField(max_length=5000)
	Community = models.ForeignKey(Community, blank=True, default=1, on_delete=models.DO_NOTHING)
	
	def __str__(self):
		return u'Workflow {0} ({1})'.format(self.Name, self.id)
	
	def __unicode__(self):
		return u'Workflow {0} ({1})'.format(self.Name, self.id)


class Task(BaseModel):
	Name = models.CharField(max_length=50)
	Description = models.CharField(max_length=5000)
	Available = models.BooleanField(default=False)
	AvailableTill = models.DateField(blank=True, null=True)
	AvailableTimes = models.IntegerField(default=0)
	Workflow = models.ForeignKey(Workflow, blank=True, on_delete=models.DO_NOTHING)
	AssignedUsers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
	AssignedRoles = models.ManyToManyField(Role, blank=True)
	Predecessors = models.ManyToManyField("self", blank=True, symmetrical=False)
	InputFields = models.ManyToManyField(DataField, related_name="InputFields", blank=True)
	OutputFields = models.ManyToManyField(DataField, related_name="OutputFields", blank=True)
	Type = models.IntegerField(choices=[(choice.value, choice.name.replace("_", " ")) for choice in TaskType])
	
	@property
	def ExecutedCount(self):
		return Execution.objects.filter(Task=self).count()
	
	@property
	def IsAvailable(self):
		if not self.Available:
			return False
		if self.AvailableTill:  # TODO Check this statement checks wheather datatime is empty of exist
			if datetime.datetime.now().date() > self.AvailableTill:
				return False
		if not self.AvailableTimes:
			if self.ExecutedCount >= self.AvailableTimes:
				return False
		return True
	
	def __str__(self):
		return u'Task {0} ({1})'.format(self.Name, self.id)
	
	def __unicode__(self):
		return u'Task {0} ({1})'.format(self.Name, self.id)


class ExecutionData(BaseModel):
	Field = models.ForeignKey(DataField, blank=True, on_delete=models.DO_NOTHING)
	DataGroup = models.ForeignKey("self", blank=True, null=True, on_delete=models.DO_NOTHING)
	Value = JSONField(default="{}")


class Execution(BaseModel):
	Task = models.ForeignKey(Task, blank=True, on_delete=models.DO_NOTHING)
	Data = models.ManyToManyField(ExecutionData, blank=True)
	ExecutedBy = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.DO_NOTHING)


class DataType(BaseModel):
	Name = models.CharField(max_length=50)
	Fields = models.ManyToManyField(DataField, blank=True)
	Community = models.ForeignKey(Community, blank=True, default=1, on_delete=models.DO_NOTHING)
	
	def __str__(self):
		return u'DataType {0} ({1})'.format(self.Name, self.id)
	
	def __unicode__(self):
		return u'DataType {0} ({1})'.format(self.Name, self.id)


class Member(BaseModel):
	Community = models.ForeignKey(Community, on_delete=models.DO_NOTHING)
	User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
	Roles = models.ManyToManyField(Role, blank=True)
	Banned = models.BooleanField(default=False)
	
	def __str__(self):
		return u'{0} is member of {1}'.format(self.User.name, self.Community.Name)
	
	def __unicode__(self):
		return u'{0} is member of {1}'.format(self.User.name, self.Community.Name)
