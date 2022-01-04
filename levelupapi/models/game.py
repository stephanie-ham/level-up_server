from django.db import models

from levelupapi.models.category import Category
from levelupapi.models.gamer import Gamer

class Game(models.Model):
    title = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    gamer = models.ForeignKey(
        Gamer,
        on_delete=models.CASCADE,
        related_name='created_games'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='games'
    )
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()