import logging

from cc.models import Category


class CategoryService(object):
	__instance = None
	__logger = logging.getLogger('CategoryService')
	
	@staticmethod
	def Instance():
		if CategoryService.__instance is None:
			CategoryService()
		return CategoryService.__instance
	
	def __init__(self):
		if CategoryService.__instance is not None:
			raise Exception("CategoryService is a singleton, use 'CategoryService.Instance()'")
		CategoryService.__instance = self
	
	def Search(self, word):
		raise NotImplementedError
	
	def Create(self, category):
		raise NotImplementedError
	
	def GetOrCreate(self, category):
		model = Category.objects.get_or_create(Name=category)
		return model