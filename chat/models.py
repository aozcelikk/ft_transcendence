from django.db import models
from django.core.exceptions import ValidationError




class Player(models.Model):
    name = models.CharField(max_length=255)

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    players = models.ManyToManyField(Player)




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
    
