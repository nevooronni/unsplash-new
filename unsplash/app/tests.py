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