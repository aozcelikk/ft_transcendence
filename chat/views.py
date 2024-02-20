from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Room
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json


@login_required
def sohbet_anasayfa(request):
    odalar = Room.objects.all()
    if request.method == 'POST':
        user = request.user.username
        option = request.POST.get('option')
        gir = request.POST.get('gir')
        room_name = request.POST.get('oda_ismi')
        if option == '1':
            game = Room.objects.filter(room_name=room_name).first()
            if game is None:
                game = Room(game_creator=user, room_name=room_name)
                game.save()
                return redirect('/sohbet/' + room_name)

            if game.player_count() >= 2:
                messages.success(request, "The room is already full or finish")
                return redirect("sohbet_anasayfa")
            
        if option == '2' :
            game = Room.objects.filter(room_name=room_name).first()
            if game is None:
                messages.success(request, "The room does not exist")
                return redirect("sohbet_anasayfa")
            if game.player_count() >= 2:
                messages.success(request, "The room is already full or finish")
                return redirect("sohbet_anasayfa")
            game.game_opponent = user
            game.save()
            return redirect('/sohbet/' + room_name)
    return render(request, 'sohbet_anasayfa.html', {'odalar':odalar})

@login_required
def sohbet_oda(request,room_name):
    game = get_object_or_404(Room, room_name=room_name)

    return render(request, "oda.html", {
        'room_name': room_name,
        'user': lambda: request.user.username if request.user.username == game.game_creator else game.game_opponent,
        'creator': game.game_creator,
        'opponent': game.game_opponent,
        'winner': game.winner,
        'game_over': game.is_over
        })

@login_required
def game_history(request):
    return render(request, "game_history.html", {'game_history': Room.objects.all()})


@login_required
def guncelleme(request, room_name):
    if request.method == 'POST':
        winner = json.loads(request.body).get('winner')
        if not winner:
            return JsonResponse({'success': False, 'error': 'Invalid request method'})
        game = get_object_or_404(Room, room_name=room_name)
        game.winner = winner
        game.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})






from .models import Tournament



def create_tournament(request):
    if request.method == "POST":
        oyuncu1 = request.POST.get('oyuncu1')
        oyuncu2 = request.POST.get('oyuncu2')
        oyuncu3 = request.POST.get('oyuncu3')
        tournament = Tournament.objects.filter(oyuncu1=oyuncu1, oyuncu2=oyuncu2, oyuncu3=oyuncu3).first()
        if tournament is None:
            tournament = Tournament(oyuncu1=oyuncu1, oyuncu2=oyuncu2, oyuncu3=oyuncu3)
        tournament.save()
        return redirect('turnuva')
    return render(request, 'create_tournament.html')



def turnuva(request):
    if request.method == "POST":
        yfinal = request.POST.get("yfinal")
        tournament = Tournament.objects.last()
        tournament.yfinal = yfinal
        tournament.save()
        return redirect('turnuva')
    return render(request,'Turnu.html', {'oyuncular':Tournament.objects.all().last()})

# def turnuva(request):
#     return render(request,'Turnu.html', {'oyuncular':Tournament.objects.all().last()})