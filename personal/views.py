from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from personal.models import Game
##from personal.models import Tag
from personal.models import List
from personal.models import Transaction
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

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
	recently_purchase=[] #last 3 purchase
	recommended_list=[]
	purchased_game_id=[]

	#Get featured list
	id_list=List.objects.filter(name='Featured List').values_list('games', flat=True)
	for i in id_list:
		featured_list.append(Game.objects.get(pk=i))

	if request.user.is_authenticated():
		#Get recommended list
		purchase_history = Transaction.objects.filter(buyer=request.user).order_by('-date')

		for i in purchase_history.values_list('game', flat=True):
			purchased_game_id.append(i)

		recently_purchase = purchase_history[:3]


		for i in recently_purchase:
			try:
				similar_games = i.game.tag.similar_objects()
				for g in similar_games:
					if not Transaction.objects.filter(buyer=request.user, game=g).exists() and g not in recommended_list:
						recommended_list.append(g)
						break
			except IndexError:
				print("No recommended game.")
			#recommended_list.append(g.tag.similar_objects()[0])
		return render(request,'personal/home.html',{'content':[Game.objects.all(),featured_list, recommended_list, recently_purchase, purchase_history]})
	else:
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

@login_required
def add_tag(request, game_id):

	tag_name = request.POST.get("t")
	if tag_name:
		g = Game.objects.get(id=game_id)
		g.tag.add(tag_name)
		##try:
			##t = Tag.objects.get(name=tag_name)
			##if not g.tag.filter(name=tag_name).exists():
				##g.tag.add(t)
		##except Tag.DoesNotExist:
			##g.tag.create(name=tag_name)

	return HttpResponseRedirect('/game/'+game_id)

@login_required
def add_review(request, game_id):
	review_text = request.POST.get("r")
	if review_text:
		now = datetime.datetime.now()
		g = Game.objects.get(id=game_id)
		g.review_set.create(text=review_text, date=now, game=game_id, writer=request.user)
	return HttpResponseRedirect('/game/'+game_id)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def purchase(request, game_id):
	g = Game.objects.get(id=game_id)
	if not Transaction.objects.filter(buyer=request.user, game=g):
		now = datetime.datetime.now()
		Transaction.objects.create(buyer=request.user, game=g, date=now)
		messages.success(request, "Successfully Purchased!")
	else:
		messages.error(request, "You have already purchased the game!")
	return HttpResponseRedirect('/game/'+game_id)
