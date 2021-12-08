from django.db import models

from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer

class Event(models.Model):

    title = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    date = models.DateField
    time = models.TimeField
