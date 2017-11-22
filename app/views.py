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

def search_results(request):
	#get all tags
	all_tags = tags.display_tags()

	if 'tag' in request.GET and request.GET['tag']:#check if photo query exists in our request.GET object
		search_term = request.GET.get('tag')#get search term
		search_images = Photo.search_by_tags(search_term)#call  our search method
		message = f"{search_term}"#capture the search term in a variable

		return render(request,'all-app/search.html',{"message":message,"tags":search_images,"all_tags":all_tags})

	else:
		message = "You haven't searched for any term"

		return render(request,'all-app/search.html',{"message":message,"all_tags":all_tags})	 

def photo(request,photo_id):
	try:
		photo = Photo.objects.get(id = photo_id)#get specific photo

	except DoesNotExist:
		raise Http404()

	return render(request,'all-app/photo.html',{"photo":photo})

def tag(request,tag_id):
	#get all tags
	all_tags = tags.display_tags()
	try:
		tag = tags.objects.get(id = tag_id)
		photos = Photo.objects.filter(tags=tag).all()

	except DoesNotExist:
		raise Http404()
	
	return render(request,'all-app/tag.html',{"tag":tag,"photos":photos,"all_tags":all_tags})

