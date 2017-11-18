from django.test import TestCase#import testcase class
from .models import User,tags,Photo

class UserTestClass(TestCase):

	#set up method
	def setUp(self):#create an instance of the editor class before every test
		self.neville = User(first_name = 'Neville',last_name = 'Oronni',email = 'nevooronni@gmail.com')

	#test the instance
	def test_instance(self):
		self.assertTrue(isinstance(self.neville,User))#test to confirm object is being instantiated correctly
	
	#test the save method
	def test_save_method(self):
		self.neville.save_user()
		users = User.objects.all()
		self.assertTrue(len(users) > 0)

	#test the delete method
	def test_delete_method(self):
		self.neville.save_user()
		self.neville.delete_user()
		users = User.objects.all()
		self.assertTrue(len(users) == 0)

	#test for display method
	def test_display_method(self):
		self.neville.save_user()
		all_users = User.display_users()
		users = User.objects.all()
		self.assertTrue(len(all_users) == len(users))

class tagsTestClass(TestCase):
	
	#set up method 
	def setUp(self):
		self.nature	= tags(name = "nature")	

	#test instance
	def test_instance(self):
		self.assertTrue(isinstance(self.nature,tags))

	#test the save method 
	def test_save_method(self):
		self.nature.save_tag()
		all_tags = tags.objects.all()
		self.assertTrue(len(all_tags) > 0)

	#test the delete method
	def test_delete_method(self):
		self.nature.save_tag()
		self.nature.delete_tag()
		all_tags = tags.objects.all()
		self.assertTrue(len(all_tags) == 0)

	#test for the display method
	def test_display_method(self):
		self.nature.save_tag()
		all_display_tags = tags.display_tags()
		all_tags = tags.objects.all()
		self.assertTrue(len(all_display_tags) == len(all_tags))

	#test if you search for tag you get it
	def test_search_method(self):
		self.nature.save_tag()
		searched_tag = tags.search_for_tag('nature')
		self.assertTrue(len(searched_tag) == 1)
