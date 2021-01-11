# Lab 9 - Crud

####
##### Wymagania dotyczące dziewiątego zadania:
####

![alt text](https://i.imgur.com/7U7n4ve.png)  


---
# Wykonanie zadań

Instalacja Cors:

![](https://i.imgur.com/GgJKii5.png)

Dodanie go do listy zainstalowanych aplikacji

![](https://i.imgur.com/QpHUKDr.png)

Middleware, wykorzystywanie zaleceń:

![](https://i.imgur.com/egTOwv8.png)

Ustawienie cors tak, aby przyjmował żądania od naszej domeny ustawionej w Whitelist:

![](https://i.imgur.com/YQt00WI.png)

Utworzenie nowego modelu, który ma tytuł opis oraz kiedy został opublikowany.

![](https://i.imgur.com/q5LOuQD.png)

Wykonane migracje:

![](https://i.imgur.com/doUzQPx.png)

Wygenerowany model:

![](https://i.imgur.com/zkYXiRa.png)

Zdefiniowalam nowe ścieżki, aby się do nich odnieść w recipes/url.py dodałam nową ścieżkę:
```
urlpatterns = [
    ...
    path('', include('recipebook.urls')),
]
```
Poszczególne ścieżki to te do przepisów, poszczególnego przepisu i tych opublikowanych.
```
urlpatterns = [ 
    url(r'^api/recipes$', views.recipe_list),
    url(r'^api/recipes/(?P<pk>[0-9]+)$', views.recipe_detail),
    url(r'^api/recipes/published$', views.recipe_list_published)
]
```
# Views
Utworzone widoki, które są używane powyżej.

1. #### recipe_list

- dla metody get

![](https://i.imgur.com/YMaTnSk.png)

- dla metody post

![](https://i.imgur.com/mgTQJqS.png)

2. #### recipe_detail

Zarządzanie przepisami, w tym wyświetlanie poszczególnych dodawanie czy usuwanie.

![](https://i.imgur.com/G7dmZeN.png)

3. #### recipe_list_published 

![](https://i.imgur.com/IpxLtMl.png)











