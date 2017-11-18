from django.contrib import admin
from .models import User,Photo,tags

class PhotoAdmin(admin.ModelAdmin):#inherits from the model admin class 
	filter_horizontal = ('tags',)#allows ordering of many to many fields and pass in tags photo field

admin.site.register(User)
admin.site.register(Photo,PhotoAdmin)#pass class as second argument in fuction so new field will appear adjacent 
admin.site.register(tags)


