import inspect
import sys
from inspect import getmembers, isclass, isabstract
from re import finditer

from cc.models import ClassEnum


class BaseFieldClass(object):
	@property
	def TemplateClass(self):
		return ClassEnum.Error
	
	def GetFunctionList(self):
		result = {}
		functions = inspect.getmembers(self, predicate=inspect.ismethod)
		
		for key, other in functions:
			if key == "GetFunctionList": continue
			matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', key)
			name = ' '.join([m.group(0) for m in matches])
			result[key] = name
		return result


class FieldClass:
	types = {}
	
	def __init__(self):
		self.__collectComparators()
	
	def Get(self, _type):
		return self.types.get(_type, None)
	
	def __collectComparators(self):
		if FieldClass.types:
			return
		comparatorClasses = getmembers(sys.modules[__name__], lambda o: isclass(o) and not isabstract(o))
		for name, _type in comparatorClasses:
			if isclass(_type) and issubclass(_type, BaseFieldClass) and not isabstract(_type):
				key = _type().TemplateClass
				FieldClass.types[key] = _type()


class UserField(BaseFieldClass):
	@property
	def TemplateClass(self):
		return ClassEnum.User
	
	def JoinCommunity(self):
		raise Exception("Not implemented")
