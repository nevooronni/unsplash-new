from django.http import HttpResponse 
import datetime as dt

# Create your views here.
def welcome(request):
	return HttpResponse('Welcome to the Moringa Tribune')

def pics_of_day(request):
	date = dt.date.today()

	#function to find exact day 
	day = convert_dates(date)
	html = f'''
				<html>
						<body>
								<h1>Pics for {day} {date.day}-{date.month}-{date.year}</h1>
						</body>
				</html>
					'''
	return HttpResponse(html)

def convert_dates(dates):#takes in date object
	#functions that gets the weekday number for the date
	day_number = dt.date.weekday(dates)#call date.weekday pass in date object

	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

	#return the actual day of the week
	day = days[day_number]
	return day 
