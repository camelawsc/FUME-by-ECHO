from django.contrib import admin
from personal.models import Game
from personal.models import Tag
from personal.models import List

admin.site.register(Tag)
admin.site.register(Game)
admin.site.register(List)