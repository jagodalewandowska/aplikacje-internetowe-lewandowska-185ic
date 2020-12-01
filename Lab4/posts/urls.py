from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    # wszystkie ścieżki będą się znajdować w api/v1, więc widok PostList
    # będzie w api/v1/#, gdzie # - klucz główny jaki będzie na wejściu.
    # jeśli id jest równe 1, wtedy ścieżka będzie wyglądać api/v1/1
    path('', PostList.as_view()),
]