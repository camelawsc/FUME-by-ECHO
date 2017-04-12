from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from personal.models import Game
from django.contrib.auth import views as auth_views

app_name = 'personal'
urlpatterns = [
	url(r'^contact/$',views.contact,name='contact'),
	url(r'^search',views.search,name='search'),
	url(r'^$',views.home,name='home'),
	url(r'^game/(?P<pk>\d+)$',DetailView.as_view(model=Game,template_name='personal/game.html')),
	url(r'^game/(?P<game_id>\d+)/add_tag$',views.add_tag,name='add_tag'),
	url(r'^game/(?P<game_id>\d+)/add_review$',views.add_review,name='add_review'),
	url(r'^genre/',views.genre,name='genre'),
    	url(r'^accounts/signup/$', views.signup, name='signup'),
    	url(r'^game/(?P<game_id>\d+)/purchase$', views.purchase, name='purchase'),
]

