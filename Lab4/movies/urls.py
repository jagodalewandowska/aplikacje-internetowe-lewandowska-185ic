from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^genres/$', GenreList.as_view()),
    url(r'^movies/$', MovieList.as_view()),
]