from datetime import datetime
from django.shortcuts import render

# Dodawanie modelu użytkownika
from django.contrib.auth import get_user_model

# import generics z Django rest framework, dodawanie restrykcji 
# aby nie pozwalać wszystkim na edycję postów
from rest_framework import generics, permissions

# Import modeli i serializerów + dodanie UserSerializera
from .models import Post
from .serializers import PostSerializer, UserSerializer

# import zezwoleń
from .permissions import IsAuthorOrReadOnly

from .serializers import PostSerializer

# Import filtrowania
from django_filters.rest_framework import DjangoFilterBackend

# Import Search
from rest_framework.filters import SearchFilter, OrderingFilter

# Import viewsets
from rest_framework import viewsets
from django.views import generic
from django.http import HttpResponse


# Wyświetlanie wszystkich postów na blogu
class PostViewSet(viewsets.ModelViewSet):
    # zezwolenia tylko dla zalogowanych użytkowników
    permission_classes = (IsAuthorOrReadOnly,)

    # wyświetlanie wszystkich postów, serializer
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # filtrowanie
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['created_at','updated_at','author']

    # kolejność
    ordering_fields =['author', 'title', 'body', 'created_at']

# Viewset dla użytkowników
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

def cookies(request):  
    html = HttpResponse("")
    if request.COOKIES.get('visits'):           
        value = int(request.COOKIES.get('visits'))
        html = HttpResponse("<h1>You've been here {} times!</h1>".format(value + 1))   
        html.set_cookie('visits', value + 1)           
        
    else:
        value = 1
        html = HttpResponse("<h1>You're here for the first time!</h1>")   
        html.set_cookie('visits', value)        
    return html

    

'''
# Aby udostępniać dodawanie, aktualizowanie oraz usuwanie postów
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # dodanie własnych zezwoleń
    permission_classes = (IsAuthorOrReadOnly,)

    # jak wyżej
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''