from django.contrib import admin

# dolaczanie modelu Post, rejestracja uzytkownika
from .models import Post

admin.site.register(Post)