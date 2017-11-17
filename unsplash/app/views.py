from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect 
import datetime as dt 

def pics_today(request):
	date = dt.date.today()

	return render(request,'all-app/today-pics.html', {"date":date})


def past_days_pics(request,past_date):#pass in request object and date from url
	
	try:
		#changes string url
		date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()#convert date url to date object

	except ValueError:
		#Raise 404 error when ValueError is thrown 
		raise Http404()
		assert False

	if date == dt.date.today():
		return redirect(pics_today)

	return render(request, 'all-app/past-pics.html', {"date":date})
