from django.shortcuts import render

# import generics z Django rest framework, dodawanie restrykcji 
# aby nie pozwalać wszystkim na edycję postów
from rest_framework import generics, permissions

# Import modeli i serializerów
from .models import Post
from .serializers import PostSerializer

# import zezwoleń
from .permissions import IsAuthorOrReadOnly

# Import filtrowania
from django_filters.rest_framework import DjangoFilterBackend

# Import Search
from rest_framework.filters import SearchFilter

# Import viewsets
from rest_framework import viewsets

# Wyświetlanie wszystkich postów na blogu
class PostViewSet(viewsets.ModelViewSet):
    # zezwolenia tylko dla wybranych użytkowników -> permission_classes = (permissions.IsAuthenticated,)

    # wyświetlanie wszystkich postów, serializer
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # filtrowanie
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['created_at','updated_at','author']

'''
# Aby udostępniać dodawanie, aktualizowanie oraz usuwanie postów
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # dodanie własnych zezwoleń
    permission_classes = (IsAuthorOrReadOnly,)

    # jak wyżej
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''