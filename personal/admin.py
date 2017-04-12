from django.contrib import admin
from personal.models import Game
from taggit.managers import TaggableManager
from personal.models import Review
from personal.models import List
from personal.models import Transaction

admin.site.register(Game)
admin.site.register(List)
admin.site.register(Review)
admin.site.register(Transaction)
