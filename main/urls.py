from django.conf.urls import url

from main.views import index, page

urlpatterns = [
	url(r'^$', index),
	url(r'^pages/(?P<id>\d+)/$',page),
    url(r'^pages/(?P<slug>[\w-]+)/$', page),
]
