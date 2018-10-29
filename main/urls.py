from django.conf.urls import url

from main.views import index, page, sponsorForm, proposalForm

urlpatterns = [
	url(r'^$', index),
	url(r'^sponsorship/',sponsorForm),
	url(r'^proposal/',proposalForm),
	url(r'^pages/(?P<id>\d+)/$',page),
    url(r'^pages/(?P<slug>[\w-]+)/$', page),
]
