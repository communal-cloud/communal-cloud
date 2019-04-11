from enum import Enum

from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone
from jsonfield import JSONField

class ClassEnum(Enum):
	Error = 0
	Integer = 1
	String = 2
	Boolean = 3
	Color = 4
	DayOfWeek = 5
	Date = 6
	Time = 7
	Empty = 8
	DateTime = 9
	Relation = 10

class BaseModel(models.Model):
	CreatedOn = models.DateTimeField()
	ModifiedOn = models.DateTimeField()
	Deleted = models.BooleanField(default = False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.CreatedOn = timezone.now()
		else:
			del self.CreatedOn
		self.ModifiedOn = timezone.now()
		return super(BaseModel, self).save(*args, **kwargs)

class Role(BaseModel):
	Name = models.CharField(max_length = 50)
	SystemDefined = models.BooleanField(default = True)

	def __str__(self):
		return u'Role {0} ({1})'.format(self.Name, self.id)

	def __unicode__(self):
		return u'Role {0} ({1})'.format(self.Name, self.id)

class Category(BaseModel):
	Name = models.CharField(max_length = 100)

	def __str__(self):
		return u'Category {0} ({1})'.format(self.Name, self.id)

	def __unicode__(self):
		return u'Category {0} ({1})'.format(self.Name, self.id)

class DataEnumeration(BaseModel):
	Name = models.CharField(max_length = 50)
	Value = JSONField(default = "{}")

	def __str__(self):
		return u'DataEnumeration {0} ({1})'.format(self.Name, self.id)

	def __unicode__(self):
		return u'DataEnumeration {0} ({1})'.format(self.Name, self.id)

class DataField(BaseModel):
	Name = models.CharField(max_length = 50)
	Type = models.IntegerField(choices = [(choice.value, choice.name.replace("_", " ")) for choice in ClassEnum])
	Enumerations = models.ManyToManyField(DataEnumeration, blank = True)
	Treasure = models.BooleanField(default = False)

	def __str__(self):
		typeName = ClassEnum(int(self.Type)).name.replace('_', ' ')
		return u'{0} DataField {1} ({2})'.format(typeName, self.Name, self.id)

	def __unicode__(self):
		typeName = ClassEnum(int(self.Type)).name.replace('_', ' ')
		return u'{0} DataField {1} ({2})'.format(typeName, self.Name, self.id)

class DataType(BaseModel):
	Name = models.CharField(max_length = 50)
	Fields = models.ManyToManyField(DataField, blank = True)

	def __str__(self):
		return u'DataType {0} ({1})'.format(self.Name, self.id)

	def __unicode__(self):
		return u'DataType {0} ({1})'.format(self.Name, self.id)

class Task(BaseModel):
	Name = models.CharField(max_length = 50)
	Description = models.CharField(max_length = 5000)
	Available = models.BooleanField(default = False)
	AvailableTill = models.DateField(blank = True)
	AvailableTimes = models.IntegerField(default = 0)
	Users = models.ManyToManyField(User, blank = True)
	Roles = models.ManyToManyField(Role, blank = True)
	Predecessors = models.ManyToManyField("self", blank = True, symmetrical = False)
	InputFields = models.ManyToManyField(DataField, related_name = "InputFields", blank = True)
	OutputFields = models.ManyToManyField(DataField, related_name = "OutputFields", blank = True)

	def __str__(self):
		return u'Task {0} ({1})'.format(self.Name, self.id)

	def __unicode__(self):
		return u'Task {0} ({1})'.format(self.Name, self.id)

class ExecutionData(BaseModel):
	Field = models.ForeignKey(DataField, blank = True, on_delete = models.CASCADE)
	DataGroup = models.ForeignKey("self", blank = True, on_delete = models.CASCADE)
	Value = JSONField(default = "{}")

class Execution(BaseModel):
	Task = models.ForeignKey(Task, blank = True, on_delete = models.CASCADE)
	Data = models.ManyToManyField(ExecutionData, blank = True)
	ExecutedBy = models.ManyToManyField(User, blank = True)

class Workflow(BaseModel):
	Name = models.CharField(max_length = 50)
	Description = models.CharField(max_length = 5000)
	Users = models.ManyToManyField(User, blank = True)
	Roles = models.ManyToManyField(Role, blank = True)
	Tasks = models.ManyToManyField(Task, blank = True)

	def __str__(self):
		return u'Workflow {0} ({1})'.format(self.Name, self.id)

	def __unicode__(self):
		return u'Workflow {0} ({1})'.format(self.Name, self.id)

class Community(BaseModel):
	Name = models.CharField(max_length = 50)
	Purpose = models.CharField(max_length = 250)
	Description = models.CharField(max_length = 5000)
	Roles = models.ManyToManyField(Role, blank = True)
	Categories = models.ManyToManyField(Category, blank = True)

	def __str__(self):
		return u'Community {0} ({1})'.format(self.Name, self.id)

	def __unicode__(self):
		return u'Community {0} ({1})'.format(self.Name, self.id)

class Member(BaseModel):
	Community = models.ForeignKey(Community, on_delete = models.CASCADE)
	User = models.ForeignKey(User, on_delete = models.CASCADE)
	Roles = models.ManyToManyField(Role, blank = True)
	Banned = models.BooleanField(default = False)

	def __str__(self):
		return u'{0} is member of {1}'.format(self.User.first_name, self.Community.Name)

	def __unicode__(self):
		return u'{0} is member of {1}'.format(self.User.first_name, self.Community.Name)
