from django.urls import path, include
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    # nie jest potrzebne w przypadku używania routers
    # path('<int:pk>/', PostDetail.as_view()),
    # wszystkie ścieżki będą się znajdować w api/v1, więc widok PostList
    # będzie w api/v1/#, gdzie # - klucz główny jaki będzie na wejściu.
    # jeśli id jest równe 1, wtedy ścieżka będzie wyglądać api/v1/1
    # path('', PostList.as_view()),
]

router = SimpleRouter()
# od teraz zamist user details jest user instance - dodatkowa opcja usuwania
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

