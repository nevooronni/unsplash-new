from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect 
import datetime as dt 
from .models import Photo,tags,User

def pics_today(request):
	#get all tags
	all_tags = tags.display_tags()

	#get all photos
	all_photos = Photo.display_photos()

	#get all photos for that day 
	date = dt.date.today()
	photos = Photo.new_photos()

	return render(request,'all-app/today-pics.html', {"date":date,"photos":photos,"all_tags":all_tags,"all_photos":all_photos})


# def past_days_pics(request,past_date):#pass in request object and date from url
	
# 	try:
# 		#changes string url
# 		date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()#convert date url to date object

# 	except ValueError:
# 		#Raise 404 error when ValueError is thrown 
# 		raise Http404()
# 		assert False

# 	if date == dt.date.today():
# 		return redirect(pics_today)

# 	return render(request, 'all-app/past-pics.html', {"date":date})
