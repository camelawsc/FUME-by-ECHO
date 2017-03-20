from django.shortcuts import render
from personal.models import Game
from personal.models import Tag
from personal.models import List
from django.db.models import Q

def index(request):
	return render(request,'personal/home.html')

def contact(request):
	return render(request,'personal/basic.html', {'content':['If you would like to cocntact me','kcfdaniel@gmail.com']})

def game(request):
	return render(request,'personal/game.html')


##In the current implementation, the title works only if there is at least a game in that genre
def genre(request):
	search_result=[]
	genre=request.path.split('/')[2].capitalize()
	for game in Game.objects.all():
		if game.genre.lower() == genre.lower():
			genre=game.genre
			search_result.append(game)
	return render(request,'personal/genre.html',{'content':[Game.objects.all(),search_result,genre]})

def home(request):
	featured_list=[]
	id_list=List.objects.filter(name='Featured List').values_list('games', flat=True)
	for i in id_list:
		featured_list.append(Game.objects.get(pk=i))
	return render(request,'personal/home.html',{'content':[Game.objects.all(),featured_list]})


def search(request):
	search_result=Game.objects.all()
	if request.user.is_staff or request.user.is_superuser:
		search_result = Game.objects.all()

	query = request.GET.get("q")
	if query:
		search_result = search_result.filter(
			Q(tag__name__icontains=query)
			)

	##search_result=[]
	##search_result.append(Game.objects.filter(tag__name=query))
	return render(request,'personal/search.html',{'content':[search_result,query,Game.objects.all()]})

