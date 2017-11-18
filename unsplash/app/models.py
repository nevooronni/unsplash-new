from django.db import models

class User(models.Model):
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

	def save_user(self):
		self.save()

	def delete_user(self):
		self.delete()

	@classmethod
	def display_users(cls):
		users = User.objects.all()
		return users

class tags(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name 

	def save_tag(self):
		self.save()

	def delete_tag(self):
		self.delete()

	@classmethod
	def display_tags(cls):
		all_tags = tags.objects.all()
		return all_tags

	@classmethod
	def search_for_tag(cls,search_input):
		tags = cls.objects.filter(name__icontains=search_input)
		return tags


class Photo(models.Model):
	title = models.CharField(max_length = 30)
	user = models.ForeignKey(User)#one to many relationship with the editor
	tags = models.ManyToManyField(tags)#many to many relationship with the tags model
	pub_date = models.DateTimeField(auto_now_add=True)#stores exact time our photos were posted to the db