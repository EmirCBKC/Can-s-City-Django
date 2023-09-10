from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def detail(request, id):
    game = Game.objects.get(id=id)
    deluxe = Game.objects.get(title=game.title, edition=2)
    ultimate = Game.objects.get(title=game.title, edition=3)

    context = {
        'game': game,
        'deluxe': deluxe,
        'ultimate': ultimate
    }

    return render(request, 'detail.html', context)


def pc(request):
    pc = Game.objects.filter(platform=1, edition=1)

    context = {
        'pc': pc,
    }

    return render(request, 'pc.html', context)


def ps5(request):
    ps5 = Game.objects.filter(platform=2, edition=1)

    context = {
        'ps5': ps5,
    }

    return render(request, 'ps5.html', context)


def xbox(request):
    xbox = Game.objects.filter(platform=3, edition=1)

    context = {
        'xbox': xbox,
    }

    return render(request, 'xbox.html', context)
