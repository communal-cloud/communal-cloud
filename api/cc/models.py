from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone

class BaseModel(models.Model):
	CreatedOn = models.DateTimeField()
	ModifiedOn = models.DateTimeField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.CreatedOn = timezone.now()
		else:
			del self.CreatedOn
		self.ModifiedOn = timezone.now()
		return super(BaseModel, self).save(*args, **kwargs)


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


class Community(BaseModel):
	Name = models.CharField(max_length=50)
	Purpose = models.CharField(max_length=250)
	Description = models.CharField(max_length=5000)
	Roles = models.ManyToManyField(Role, blank=True)
	Categories = models.ManyToManyField(Category, blank=True)

	def __str__(self):
		return u'Community {0} ({1})'.format(self.Name, self.id)

	def __unicode__(self):
		return u'Community {0} ({1})'.format(self.Name, self.id)