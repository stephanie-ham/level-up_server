from django.db import models

from levelupapi.models.gamer import Gamer

class Game(models.Model):

    title = models.CharField(max_length=100)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)