from django.db import models

class Editor(models.Model):
	first_name = models.CharField(max_length = 30)#string field for small to large sized strings passes a required argument max_length
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()

