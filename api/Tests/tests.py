from django.test import TestCase

from cc.models import User
from cc.Controllers.UserController import UserAPIViewController
from cc.Services.UserService import UserService
from cc.Services.CommunityService import CommunityService
from cc.models import Community


class Test(TestCase):
	user = {
			"username": "Jane Doe",
			"email": "janedoe@fake.com",
			"password": "123456",
			"name": "Jane Doe"
		   }
	
	community = {
					"Name":"Coffee Lovers",
					"Description": "Loves to drink coffee!",
					"Categories":["coffee", "photography"],
					"Roles":[
						"Coffee Gourmet"
					]
				}
	
	__userService = UserService.Instance()
	__communityService = CommunityService.Instance()
	
	def test_register(self):
		registered_user = self.__userService.Register(self.user)
		expected_user = User.objects.last()
		self.assertEqual(registered_user.email, expected_user.email)

	def test_createCommunity(self):
		registered_user = self.__userService.Register(self.user)
		expected_user = User.objects.last()
		community_created = self.__communityService.Create(self.community, expected_user)
		self.assertEqual(community_created.Name, self.community.get("Name"))
	
	def test_updateCommunity(self):
		registered_user = self.__userService.Register(self.user)
		expected_user = User.objects.last()
		community_created = self.__communityService.Create(self.community, expected_user)
		community_updated = {
								"Name":"Tea Lovers",
								"Description": "Loves to drink tea!",
								"Categories":["tea", "photography"],
								"Roles":[
									"Tea Gourmet"
								]
							}
		updated = self.__communityService.Update(community_updated, community_created.id)
		self.assertEqual(community_updated.get("Name"), updated.Name)
	