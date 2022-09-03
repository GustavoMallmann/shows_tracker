from dataclasses import field
from django.db import models
# Create your models here.

class Show(models.Model):

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True, default='')
    imdb_rating = models.FloatField(blank=True, null=True)
    n_of_seasons = models.PositiveSmallIntegerField(blank=True, default=0)
    n_of_episodes = models.PositiveIntegerField(blank=True, default=0)
    has_ended = models.BooleanField(blank=True, null=True)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.name
    

class User_show_info(models.Model):

    show = models.OneToOneField('Show', on_delete=models.CASCADE, primary_key=True)
    user_rating = models.FloatField()
    last_episode_seen = models.PositiveSmallIntegerField(blank=True, null=True)
    last_season_seen = models.PositiveSmallIntegerField(blank=True, null=True)
    seen_all_available = models.BooleanField(blank=True, default=False)
    user_comment = models.CharField(max_length=2048, blank=True, default='')
    favorite_episode = models.ForeignKey('Episode', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.show.__str__()


class Season(models.Model):

    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True, default='')
    imdb_rating = models.FloatField(blank=True, null=True)
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.show.__str__()} {self.number}'


class Episode(models.Model):

    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True, default='')
    imdb_rating = models.FloatField(blank=True, null=True)
    number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.season.__str__()} {self.number}'

class Genre(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
