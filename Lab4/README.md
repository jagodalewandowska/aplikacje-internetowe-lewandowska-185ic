# Lab 4 - REST API z DRF

Wykorzystanie Django REST Framework. Dodanie Swaggera.

####
##### Wymagania dotyczące czwartego zadania:
####

![alt text](https://i.imgur.com/TwbYQN0.png)  


---
# Realizacja kodu z zajeć wraz z małymi modyfikacjami

Jedną z dwóch utworzonych aplikacji w projekcie to posts. Do analizy rozpoczynam od obiektu PostList. To tutaj widnieją wszystkie posty, a także jest możliwe dodawanie nowych. Jeśli użytkownik jest niezalogowany nie są wyświetlane żadne z istniejących elementów. Podląg dodanych postów w panelu administratora:

![alt text](https://i.imgur.com/n7nPXtN.png)

## Dodawanie posta

Jako zalogowany użytkownik, można dodać nowy post.

![alt text](https://i.imgur.com/1toV43L.png)  

Post widnieje na liście jako dodany.

![alt text](https://i.imgur.com/b4ST7gk.png)

Na stronie możliwe jest również filtrowanie postów oraz wyszukiwanie.

- Wybranie wyszukiwania postów stworzonych przez użytkownika "Jagoda", rezultat:

![alt text](https://i.imgur.com/mUWp33h.png)  

- Dodanie wyszykiwania, dla przykłady tytuły "rosnąco" - więc alfabetycznie.

![alt text](https://i.imgur.com/t4JE9q6.png)

Zakładka GET pozwala na pobranie postów w postaci JSON.

## Zezwolenia - permissions

Za pomocą wbudowanych zezwoleń w Django Rest możliwe jest manipulowanie tym, co widzą użytkownicy zalogowani czy mogą posty dodawać, edytować oraz usuwać. Dzięki temu można ustalać odpowiednie uprawnienia dla użytkowników w zależności czy są administratorami, czy nie oraz ograniczyć zezwolenia dla niezalogowanych użytkowników. W przykładzie poniżej tylko osoba, która utworzyła post może go edytować, w przeciwnym razie można go tylko odczytać.

Aby możliwa była ta funkcja utworzona została klasa
```
class IsAuthorOrReadOnly(permissions.BasePermission)
```

By edytować dostęp do poszczególnych klas, takich jak posty, czy w późniejszej części - aplikacji stworzonej przeze mnie, można korzystać z następujących zezwoleń:
- AllowAny - każdy użytkownik ma pełen dostęp
- IsAuthenticated - tylko zalogowani użytkownicy
- IsAdminUser - tylko administrator
- IsAuthenticatedOrReadOnly - niezalogowani użytkownicy mogą tylko przeglądać stronę, zalogowani dodawać, edytować i usuwać

Dodawane są one w obiektach jak na przykładzie postów PostViewSet, a następnie można ją ustawić, jak tutaj, używając wyżej wymienione wartości:
```
...
class PostViewSet(viewsets.ModelViewSet):
    # zezwolenia tylko dla zalogowanych użytkowników
    permission_classes = (IsAuthorOrReadOnly,)
    ...
```

Dla przykładu dodałam nowy post jako "Magdalena", wchodząc do api/v1/4 jest on widoczny, a także można go edytować i usuwać.

![alt text](https://i.imgur.com/JHu6w9p.png)

Po wylogowaniu te opcje nie są już dostępne (np. przycisk delete zniknął). Niezalogowany użytkownik może tylko dodawać posty, ale nie ma dostępu do usuwania ani edycji.

![alt text](https://i.imgur.com/yagKZCx.png)

1. ### Użytkownik niezalogowany

Zmieniłam ustawienia tak, aby użytkownik niezalogowany nie mógł już widzieć dodanych postów, zmieniając wyżej wymieniony kawałek kodu na taki:
```
permission_classes = (permissions.IsAuthenticated,)
```

Posty nie są już widoczne:

![alt text](https://i.imgur.com/ogsbuQY.png)  

2. ### Użytkownik zalogowany

![alt text](https://i.imgur.com/f2tound.png) 

## Routers
Wyróżniamy dwa rodzaje Routers - Simple oraz Default. Pozwalają one na automatyczne ustawianie ścieżek URL.
Dzięki użyciu routers, możliwe jest pominięcie zapisu:

```
 path('<int:pk>/', PostDetail.as_view()),
```

Od teraz, możliwe jest przejście do wybranego posta dopisując jego id po "/". Dostęp do poszczególnych elementów strony jest znacznie ułatwiony, jednocześnie kod staje się zdecydowane bardziej przejrzysty.


Wyświetlenie drugiego posta, dopisując "2" w adresie.

![alt text](https://i.imgur.com/H8kThPR.png)

Możliwe jest to dzięki dodaniu fragmentu kodu:

```
urlpatterns = [
    # pozostaje pusty
]

router = SimpleRouter()
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls
```

## Swagger

W zadaniu wymagane było również dodanie Swaggera, który umożliwia dokładnie badanie elementów utworzonych przy pomocy REST API. Dostępne są następujące ścieżki, opisane również w kodzie:
- /swagger.json to widok json

![alt text](https://i.imgur.com/FcprWWh.png)

- /swagger.yaml to widok yaml

- /redoc to widok redoc

![alt text](https://i.imgur.com/bccJRbt.png)
Wszystkie informacje na temat utworzonych obiektów i struktur są dokładnie podane. Przykład dla tworzenia nowego postu i odpowiedzi:

![alt text](https://i.imgur.com/zrESK2V.png)

Przykłady dla drugiej części zadania, którą było utworzenie własnej aplikacji (jest to w moim przypadku aplikacja Movies, a w niej modele Movie oraz Genre. Widać go tutaj:

![alt text](https://i.imgur.com/lqBx0LF.png)

- /swagger to widok swagger ui

![alt text](https://i.imgur.com/pDmKx31.png)

Widok modeli Post, Genre oraz Movie, które należą do aplikacji drugiej -- tej utworzonej przeze mnie, do której przejdę w dalszej części Readme.

![alt text](https://i.imgur.com/irs9A2i.png)