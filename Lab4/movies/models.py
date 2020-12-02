from django.db import models

# gatunek
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Movie(models.Model):    
    name = models.CharField(max_length=200)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    review = models.FloatField(default=1.0)
    describtion = models.TextField()
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
