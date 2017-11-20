from django.db import models
import datetime as dt

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
	image = models.ImageField(upload_to = 'photos/')

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
	def search_for_tag(cls,search_term):
		tags = cls.objects.filter(name__icontains=search_input)
		return tags


class Photo(models.Model):
	title = models.CharField(max_length = 30)
	user = models.ForeignKey(User)#one to many relationship with the editor
	tags = models.ManyToManyField(tags)#many to many relationship with the tags model
	pub_date = models.DateTimeField(auto_now_add=True)#stores exact time our photos were posted to the db
	image = models.ImageField(upload_to = 'photos/')

	def __str__(self):
		return self.title

	def save_photo(self):
		self.save()

	def delete_photo(self):
		self.delete()

	@classmethod
	def display_photos(cls):
		all_photos = Photo.objects.all()
		return all_photos

	@classmethod
	def new_photos(cls):
		today = dt.date.today()#gets todays photos
		photos = cls.objects.filter(pub_date__date = today)#query db to filter the phoost according to date date converts our datetimefield into a date(two underscores definition)
		return photos

	@classmethod
	def search_by_title(cls,search_term):
		photo = cls.objects.filter(tags__icontains=search_term)
		return photo



