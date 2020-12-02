from django.conf.urls import url
from .views import GenreList, MovieList, MovieViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    url(r'^genres/$', GenreList.as_view()),
    url(r'^movies/$', MovieList.as_view()),
]

# aby móc wyświetlać movies/1, movies/2, 
# ... bez używania <int:pk>/, api/v2/2 ...
router = SimpleRouter()
router.register('', MovieViewSet, basename='movieset')

urlpatterns += router.urls
