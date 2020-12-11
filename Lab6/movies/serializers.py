from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

# dodane wszystkie wartości oprócz id
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','name', 'genre', 'review', 'describtion', 'director', 'producer')