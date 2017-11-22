from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
	#url('^$',views.welcome,name = 'welcome'),
	url('^$',views.pics_today,name = 'picsToday'),
	url(r'^photo/(\d+)',views.photo,name = 'photo'),#capture an integer which will the  the di of the photo 
	url(r'^tag/(\d+)',views.tag,name = 'tag'),
	url(r'^search/',views.search_results,name = 'search_results')
	#url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pics,name = 'pastPics')
]

urlpatterns +=staticfiles_urlpatterns()

if settings.DEBUG:#reference to the location of uploaded files
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#app registeres the media root to upload images