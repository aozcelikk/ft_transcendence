from django.db import models
from django.core.exceptions import ValidationError

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    room_name = models.CharField(max_length=255, unique=True, default='')
    player1_paddle_position = models.IntegerField(default=0)
    player2_paddle_position = models.IntegerField(default=0)
    game_creator = models.CharField(max_length=100)
    game_opponent = models.CharField(max_length=100, blank=True, null=True)
    ball_position = models.JSONField(default=dict)
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    


def validate_room_code(value):
    if not value.isascii() or not value.isalnum() or len(value) >= 100:
        raise ValidationError("Invalid room code")


# class TicTacToe(models.Model):
#     room_code = models.CharField(max_length=100, validators=[validate_room_code])
#     game_creator = models.CharField(max_length=100)
#     game_opponent = models.CharField(max_length=100, blank=True, null=True)
#     is_over = models.BooleanField(default=False)
#     winner = models.CharField(max_length=100, blank=True, null=True)

#     def player_count(self):
#         count = 0
#         if self.game_creator:
#             count += 1
#         if self.game_opponent:
#             count += 1
#         return count
