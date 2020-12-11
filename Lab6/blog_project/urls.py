# Django REST zajmuje się transformoawaniem modelami baz danych w RESTful API 
# urls.py zajmuje się ścieżkami URL - endpoints
from django.contrib import admin
# dodanie path, by móc korzystać z posts.urls
from django.urls import include, path, re_path
# swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API for AMW",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # panel admina
   path('admin/', admin.site.urls),

   # api/v1 oznacza wersję naszego api, w przypadku kiedy chce
   # się aktualizować zapobiega to zacinaniu się, bez psucia
   # poprzednich wersji

   #       api/v1 dotyczy postów
   path('api/v1/', include('posts.urls')),

   #       api/v2 dotyczy filmów
   path('api/v2/', include('movies.urls')),

   # path może być jakakolwiek zamiast api-auth, ważne żeby zawarta
   # była składania rest_framerwork.urls. dzięki temu widoczna 
   # jest strzałka obok usera
   path('api-auth/', include('rest_framework.urls')),    

   # dodanie 3-rd party app
   path('api/v1/rest-auth/', include('rest_auth.urls')),

   # Rejestracja użytkownika -> route
   path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),

   # swagger urls, gdzie:
   # -> /swagger.json to widok json
   # -> /swagger.yaml to widok yaml
   # -> /redoc to widok redoc
   # -> /swagger to widok sawgger ui    
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
