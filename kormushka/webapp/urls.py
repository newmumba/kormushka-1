from django.conf.urls import patterns, include, url

urlpatterns = patterns('webapp.views',
	url(r'^$','index'),
	url(r'^addpurchase/$','addpurchase'),
)