from django.db import models
from django.core.exceptions import ValidationError

from django.shortcuts import render
from .models import Tournament, Player

def leaderboard(request):
    players = Player.objects.all().order_by('-won_tournaments__count', '-runner_up_tournaments__count', '-third_place_tournaments__count')
    context = {'players': players}
    return render(request, 'leaderboard.html', context)


class Room(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    game_creator = models.CharField(max_length=100)
    game_opponent = models.CharField(max_length=100, blank=True, null=True)
    is_over = models.BooleanField(default=False)
    winner = models.CharField(max_length=100, blank=True, null=True)

    def player_count(self):
        count = 0
        if self.game_creator:
            count += 1
        if self.game_opponent:
            count += 1
        return count

    def __str__(self):
        return self.room_name
    
