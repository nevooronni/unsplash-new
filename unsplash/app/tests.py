from django.test import TestCase#import testcase class
from .models import Editor,tags,Photo

class EditorTestClass(TestCase):

	#set up method
	def setUp(self):#create an instance of the editor class before every test
		self.neville = Editor(first_name = 'Neville',last_name = 'Oronni',email = 'nevooronni@gmail.com')

	#test the instance
	def test_instance(self):
		self.assertTrue(isistance(self.neville,Editor))#test to confirm object is being instantiated correctly
	

