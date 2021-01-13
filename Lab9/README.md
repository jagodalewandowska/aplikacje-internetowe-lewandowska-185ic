# Lab 9 - Django + React (aplikacja Crud)

####
##### Wymagania dotyczące dziewiątego zadania:
####

![alt text](https://i.imgur.com/7U7n4ve.png)  


---
# Strona z przepisami - RecipeBook

![](https://i.imgur.com/a0hQMhl.png)

# Wykonanie zadań - Backend

Instalacja Cors:

![](https://i.imgur.com/GgJKii5.png)

Dodanie go do listy zainstalowanych aplikacji

![](https://i.imgur.com/QpHUKDr.png)

Middleware, wykorzystywanie zaleceń:

![](https://i.imgur.com/egTOwv8.png)

Ustawienie cors tak, aby przyjmował żądania od naszej domeny ustawionej w Whitelist:

![](https://i.imgur.com/MEOcWmR.png)

Utworzenie nowego modelu, który ma tytuł opis oraz kiedy został opublikowany.

![](https://i.imgur.com/q5LOuQD.png)

Wykonane migracje:

![](https://i.imgur.com/doUzQPx.png)

Wygenerowany model:

![](https://i.imgur.com/S6flJYk.png)

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

1. ### recipe_list

- dla metody get

![](https://i.imgur.com/JcgE644.png)

- dla metody post

![](https://i.imgur.com/mgTQJqS.png)

2. ### recipe_detail

Zarządzanie przepisami, w tym wyświetlanie poszczególnych dodawanie czy usuwanie.

![](https://i.imgur.com/G7dmZeN.png)

3. ### recipe_list_published 

![](https://i.imgur.com/IpxLtMl.png)

# Frontend

Dla frontendu istenieje plik .css modyfikujący nieco widok strony, natomiast w pasku nawigacji można dodawać nowy przepis czy przeglądać wszystkie. Do utworzenia tras został użyty Route, Switch oraz Link. Zaimportowane zostały również trzy komponenty odpowiadające za modyfikację przepisów, ich dodawanie czy usuwanie.
```
import { Switch, Route, Link } from "react-router-dom";
import AddRecipe from "./components/add-recipe.component";
import Recipe from "./components/recipe.component";
import RecipeList from "./components/recipe-list.component";
```
### Komponenty:
- **add-recipe.component** - odpowiada za dodawanie nowego przepisu (tytułu, sposobu przygotowania), a jeśli zostanie wciśnięty przycisk dodaj wywołuje napis "Wysłano poprawnie":
```
...
<div className="submit-form">
        {this.state.submitted ? (
          <div>
            <h4>Wysłano poprawnie!</h4>
            <button className="btn btn-warning" onClick={this.newRecipe}>
              Dodaj
            </button>
          </div>
        ) : (
        
        // jeśli nie wysłano -----
        
          <div className="colourme">
            <div className="form-group">
              <label htmlFor="title">Przepis na:</label>
              ...
```

- **recipe-list.component** - odpowiada on za wyszukiwanie przepisów, wykorzystując odświeżanie listy, usuwanie wszystkich elementów, wybieranie aktywnego przepisu. Wyświetla on również listę przepisów jak i szczegóły. 

- **recipe-component** - odpowiada za edycję poszczególnych wpisów, gdzie można wybrać również zmianę jego statusu oraz usunąć pojedynczy wpis.

![](https://i.imgur.com/IHAwtt0.png)

# Działanie strony

Strona główna, dla przykładu dodam nowy przepis.

![](https://i.imgur.com/vmNtwQr.png)

### Dodawanie nowego wpisu

Dodanie nazwy przepisu oraz sposobu przygotowania:

![](https://i.imgur.com/TRVqv6f.png)

Efekt po dodaniu:

![](https://i.imgur.com/ghQp1Vu.png)

![](https://i.imgur.com/VRiJFvH.png)

Nowy przepis znajduje się na stronie:

![](https://i.imgur.com/7COCNIo.png)

### Wyszukiwanie

Chcąc go wyszukać wpisuję słowo **pigs** w pole wyszukiwania.

![](https://i.imgur.com/4qXOhpf.gif)

Tak więc przepis jest wyszukany, a efekt widać w konsoli:

![](https://i.imgur.com/Ew52c2f.png)

![](https://i.imgur.com/pVtZd2N.png)

### Edycja

Podczas edycji można opublikować post, usunąć go, lub aktualizować.

![](https://i.imgur.com/0MhHsLN.png)

Zmieniłam jego nazwę, a następnie opublikowałam:

![](https://i.imgur.com/YaMX3QL.png)

Jego status na stronie się zmienił, a także jego tytuł:

![](https://i.imgur.com/rNWUpaG.png)

Można go powtórnie zmienić na oczekujący:

![](https://i.imgur.com/vOHBGoZ.gif)

Podczas wykonania "update" otrzymana zostaje również informacja o pomyślnej edycji:

![](https://i.imgur.com/Volpiuh.png)

### Usuwanie przepisu

Usuwanie przepisu na pierogi:

![](https://i.imgur.com/tpIpl3Q.gif)  


---

Wszystkie przepisy widoczne są również pod **localhost:8080/api/recipes/**.

![](https://i.imgur.com/ZCTswjC.png)

Id dodanego przepisu na Pigs in blankets to 7, go również można znaleźć pod adresem **localhost:8080/api/recipes/7**.

![](https://i.imgur.com/YJmDhEH.png)