from django.conf.urls import url
from .views import GenreList, MovieViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    url(r'^genres/$', GenreList.as_view()),
    # url(r'^movies/$', MovieList.as_view()),
]

# aby móc wyświetlać api/v2/2
# ... bez używania <int:pk>/
router = SimpleRouter()
router.register('', MovieViewSet, basename='movieset')

urlpatterns += router.urls
