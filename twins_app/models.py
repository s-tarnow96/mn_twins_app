from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, models.SET_DEFAULT, default="Free Agent")


class Season(models.Model):
    year = models.IntegerField(max_length=4)

