from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from personal.models import Game

urlpatterns = [
	url(r'^contact/$',views.contact,name='contact'),
	url(r'^search',views.search,name='search'),
	url(r'^$',views.home,name='home'),
	url(r'^game/(?P<pk>\d+)$',DetailView.as_view(model=Game,template_name='personal/game.html')),
	url(r'^genre/',views.genre,name='genre'),
]