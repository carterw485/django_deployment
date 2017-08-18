from django.conf.urls import url
from apps.groups import views
urlpatterns = [
	url(r'^$', views.logIn, name='main'),
	url(r'^users/$', views.logOrganizer, name='register'),
	url(r'^users/login/$', views.logOrganizer, name='login'),
	url(r'^users/logout/$', views.logout, name='logout'),
	url(r'^groups/$', views.multiOrganizer, name='index'),
	url(r'^groups/$', views.multiOrganizer, name='create'),
	url(r'^groups/(?P<id>\d+)/$', views.singleOrganizer, name='show'),
	url(r'^groups/(?P<id>\d+)/$', views.singleOrganizer, name='update'),
	url(r'^groups/(?P<id>\d+)/$', views.singleOrganizer, name='destroy'),
	url(r'^members/(?P<group_id>\d+)/$', views.members, name='add'),
	url(r'^members/(?P<group_id>\d+)/leave/$', views.membersLeave, name='leave'),
]