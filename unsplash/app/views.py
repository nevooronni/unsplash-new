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

	if 'tag' in request.GET and request.GET['tag']:#check if photo query exists in our request.GET object
		search_input = request.GET.get('tag')#get search term
		search_tag = tags.search_for_tag(search_input)#call  our search method
		single_tag = searched_tags[0]#single tag
		photos = Photo.objects.filter(tags=single_tag).all()
		message = f"{search_term}"#capture the search term in a variable

		return render(request,'all-app/search.html',{"message":message,"photos":searched_photos,"tags":search_tag})

	else:
		message = "You haven't searched for any term"

		return render(request,'all-app/search.html',{"message":message})	 

def photo(request,photo_id):
	try:
		photo = Photo.objects.get(id = photo_id)#get specific photo

	except DoesNotExist:
		raise Http404()

	return render(request,'all-app/photo.html',{"photo":photo})

def tag(request,tag_id):
	try:
		tag = tags.objects.get(id = tag_id)
		photos = Photo.objects.filter(tags=tag).all()

	except DoesNotExist:
		raise Http404()
	
	return render(request,'all-app/tag.html',{"tag":tag,"photos":photos})

