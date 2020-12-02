from django.shortcuts import render

# import modeli
from django.contrib.auth.models import User
from rest_framework import generics, permissions

# Import modeli i serializerów
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer

# Import filtrowania
from django_filters.rest_framework import DjangoFilterBackend


class GenreList(generics.ListCreateAPIView):
    # Lista oraz tworzenie nowych gatunków
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # tylko administrator może zarządzać gatunkami filmów
    permission_classes = (permissions.IsAdminUser, )

class MovieList(generics.ListCreateAPIView):
    # Lista oraz tworzenie filmów
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )

    # filtrowanie
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review', 'genre', 'director', 'producer']



