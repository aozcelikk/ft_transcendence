from django.db import models
from django.core.exceptions import ValidationError


class Tournament(models.Model):
    oyuncu1 = models.CharField(max_length=255, null=True)
    oyuncu2 = models.CharField(max_length=255, null=True)
    oyuncu3 = models.CharField(max_length=255, null=True)
    yfinal = models.CharField(max_length=255, null=True)
    kazanan = models.CharField(max_length=255, null=True)




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
    
