from django.db import models

from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer

class Event(models.Model):
    organizer = models.ForeignKey(
        Gamer,
        on_delete=models.CASCADE,
        related_name='organizer'
    )
    description = models.CharField(max_length=200)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='events'
    )
    date = models.DateField()
    time = models.TimeField()
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value