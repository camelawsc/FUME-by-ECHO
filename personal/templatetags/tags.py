from django.shortcuts import render
from personal.models import Game
from django import template

register=template.Library()

@register.inclusion_tag('personal/navigation.html')
def navigation(selected_id=None):
    return {
        'navigation': Game.objects.all(),
        'selected':selected_id,
    }