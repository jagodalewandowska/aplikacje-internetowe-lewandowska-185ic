# Django REST zajmuje się transformoawaniem modelami baz danych w RESTful API 
# urls.py zajmuje się ścieżkami URL - endpoints
from django.contrib import admin
# dodanie path, by móc korzystać z posts.urls
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # api/v1 oznacza wersję naszego api, w przypadku kiedy chce
    # się aktualizować zapobiega to zacinaniu się, bez psucia
    # poprzednich wersji
    path('api/v1/', include('posts.urls')),
    # path może być jakakolwiek zamiast api-auth, ważne żeby zawarta
    # była składania rest_framerwork.urls. dzięki temu widoczna 
    # jest strzałka obok usera
    path('api-auth/', include('rest_framework.urls')),
]
