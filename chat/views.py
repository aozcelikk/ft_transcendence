from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import TicTacToe
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json



def tictac(request):
    if request.method == 'POST':
        user = request.user.username
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')

        if option == '1':
            game = TicTacToe.objects.filter(room_code=room_code).first()
            if game is None:
                messages.success(request, "Room code not found")
                return HttpResponseRedirect('/tictac')

            if game.player_count() >= 2:
                messages.success(request, "The room is already full")
                return HttpResponseRedirect('/tictac')

            game.game_opponent = user
            game.save()
            return redirect('/tictac/' + room_code)

        elif option == '2':
            game = TicTacToe.objects.filter(room_code=room_code).first()
            if game is None:
                game = TicTacToe(game_creator=user, room_code=room_code)
                game.save()
                return redirect('/tictac/' + room_code)

            if game.player_count() >= 2:
                messages.success(request, "The room is already full")
                return HttpResponseRedirect('/tictac')

    return render(request, "front.html")


def play(request, room_code):
    game = get_object_or_404(TicTacToe, room_code=room_code)

    return render(request, "play.html", {
        'room_code': room_code,
        'user': lambda: request.user.username if request.user.username == game.game_creator else game.game_opponent,
        'creator': game.game_creator,
        'opponent': game.game_opponent,
        'winner': game.winner
        })



def update_winner(request, room_code):
    if request.method == 'POST':
        winner = json.loads(request.body).get('winner')
        if not winner:
            return JsonResponse({'success': False, 'error': 'Invalid request method'})
        game = get_object_or_404(TicTacToe, room_code=room_code)
        game.winner = winner
        game.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})