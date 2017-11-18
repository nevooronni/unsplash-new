from django.db import models

class Editor(models.Model):
	first_name = models.CharField(max_length = 30)#string field for small to large sized strings passes a required argument max_length
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()

	# try:
	# 	editor = Editor.objects.get(email = 'example@gamil.com')
	# 	print('Editor found')
	# except DoesNotExist:
	# 	print('Editor was not found')

	def __str__(self):#makes it easier to read our models in the shell return a string representation of our model 
		return self.first_name
	class Meta:
		ordering = ['first_name']#specifying model specific options 

class tags(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name 

class Photo(models.Model):
	title = models.CharField(max_length = 30)
	editor = models.ForeignKey(Editor)#one to many relationship with the editor
	tags = models.ManyToManyField(tags)#many to many relationship with the tags model
	pub_date = models.DateTimeField(auto_now_add=True)#stores exact time our photos were posted to the db