from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username


class Genre(models.Model):
    name = models.CharField(max_length=50)
    num = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    poster_url = models.TextField()
    director = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    description = models.TextField()
    grade = models.CharField(max_length=50)
    running_time = models.IntegerField()
    score = models.FloatField()
    released_date = models.IntegerField(null=True)
    genre = models.ForeignKey(Genre, related_name="movie", on_delete = models.CASCADE)
    is_excepted = models.BooleanField(default=False)
    is_rereleased = models.BooleanField(default=False)
    total_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Vote(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    who_voted = models.ManyToManyField(UserExtension, blank=True)
    
    