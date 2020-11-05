# Tutaj importujemy funkcje path Django i wszystkie nasze widoki (views) z aplikacji blog. 
from django.urls import path
from . import views

#  przyporządkowujemy widok (view) o nazwie post_list do strony głównej. 
# Ten wzorzec URL zostanie dopasowany do pustego ciągu znaków, a Django zignoruje nazwę domeny (np. http://127.0.0.1:8000/)
# name='post_list jest nazwą URL, która będzie używana do zidentyfikowania widoku
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
