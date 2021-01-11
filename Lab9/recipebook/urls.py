from django.conf.urls import url 
from recipebook import views 

# utworzenie trzech ścieżek
urlpatterns = [ 
    url(r'^api/recipes$', views.recipe_list),
    url(r'^api/recipes/(?P<pk>[0-9]+)$', views.recipe_detail),
    url(r'^api/recipes/published$', views.recipe_list_published)
]