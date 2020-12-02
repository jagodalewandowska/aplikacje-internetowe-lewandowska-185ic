# Lab 4

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

Dodane one również zostały w przypadku aplikacji drugiej - Movies. Dzięki niej można wyświetlać odpowiednie filmy po ich id bez dodawania wcześniejszego fragmentu kodu.

![alt text](https://i.imgur.com/ZHgjDAB.png)

## Swagger

W zadaniu wymagane było również dodanie Swaggera, który umożliwia dokładnie badanie elementów utworzonych przy pomocy REST API. Dostępne są następujące ścieżki, opisane również w kodzie:

- **/swagger.json** to widok json

![alt text](https://i.imgur.com/FcprWWh.png)

- **/swagger.yaml** to widok yaml, pobrany plik przy przejściu do strony:

![alt text](https://i.imgur.com/p7o9YvH.png)

- **/redoc** to widok redoc

![alt text](https://i.imgur.com/bccJRbt.png)
Wszystkie informacje na temat utworzonych obiektów i struktur są dokładnie podane. Przykład dla tworzenia nowego postu i odpowiedzi:

![alt text](https://i.imgur.com/zrESK2V.png)

Przykłady dla drugiej części zadania, którą było utworzenie własnej aplikacji (jest to w moim przypadku aplikacja Movies, a w niej modele Movie oraz Genre. Widać go tutaj:

![alt text](https://i.imgur.com/lqBx0LF.png)

- **/swagger** to widok swagger ui

![alt text](https://i.imgur.com/pDmKx31.png)

Widok modeli **Post**, **Genre** oraz **Movie**, które należą do aplikacji drugiej -- tej utworzonej przeze mnie, do której przejdę w dalszej części Readme.

![alt text](https://i.imgur.com/irs9A2i.png)


## Serializery

Serializery służą do zarządzania zawartością wyświetlaną dla użytkownika. Dla przykładu mając listę postów, można zdeklarować, że dana wartość nie ma być wyświetlana. Utworzony obiekt wraz z komentarzem wygląda następująco:
```
# include - czyli zawarte będą id, autor, tytuł, post, kiedy utworzono
# exclude - updated_at nie jest zawarte w fields
        fields = ('id', 'author', 'title', 'body', 'created_at',)
```
Dlatego w liście widać tylko id, autor, tytuł ... ale nie **updated_at**.

![alt text](https://i.imgur.com/SwWdS4k.png)  




---
# Własna aplikacja Movies

Aplikacja zawiera Obiekty Genre - które przy tworzeniu Movies można wykorzystywać z listy, dodając nową pozycję. Stan początkowy to:

![alt text](https://i.imgur.com/GinUapw.png)

A także listę 12 filmów, które mają nadane wartości z obiektu gatunek.

![alt  text](https://i.imgur.com/XpuqKdn.png)

Zezwolenia ustawiłam tak, aby tylko administrator mógł zarządzać obiektami typu Gatunek.

- Widok **użytkownika niezalogowanego** - który nie może przeglądać gatunków, ale może widzieć filmy, lecz ich nie dodawać.

![alt text](https://i.imgur.com/VKMgHL6.png)

Brak uprawnień do dodawania filmów:

![alt text](https://i.imgur.com/iDdC6a2.png)

- Widok użytkownika **Magdalena**

![alt text](https://i.imgur.com/TjehWc3.png)

- Widok **administratora** - Jagoda

![alt text](https://i.imgur.com/mj8SCnB.png)

## Dodawanie nowego gatunku oraz filmu

Dodawanie nowego gatunku jako administrator:

![alt text](https://i.imgur.com/V6NByCI.png)

Dodawanie nowego filmu:

![alt text](https://i.imgur.com/smmP2GY.png)


## Serializery dla aplikacji Movies

Wyświetlane są wszystkie atrybuty:

![alt text](https://i.imgur.com/foHzCn7.png)

Można by było zastosować formę exclude i usuwając np. producer z listy nie byłby już on wyświetlany.

## Viewset 

Viewset jaki stworzyłam dla nowej aplikacji to ten wyświetlający listę filmów o nazwie MovieViewSet. Obiekty typu ViewSet nie posiadają metod takich jak get() czy post(), ale posiadają list() oraz create().

![alt text](https://i.imgur.com/wHkCdz1.png)

Dzięki temu wykorzystałam w późniejszym kroku ten widok w tworzeniu route:

```
...
router = SimpleRouter()
router.register('', MovieViewSet, basename='movieset')

urlpatterns += router.urls
...
```

## Sortowanie i filtrowanie, oraz wyszukiwanie

Aby uporządkować filmy względem ich oceny wybrana opcja to review - ascending.

![alt text](https://i.imgur.com/U8jRuOY.png)

Posortowane filmy wraz z rosnącą oceną:

![alt text](https://i.imgur.com/SCLxuQw.png)

Wyszukiwanie tylko filmów Star Wars:

![alt text](https://i.imgur.com/yQ4uOLc.png)

Filmy Star Wars:

![alt text](https://i.imgur.com/qDNhjWt.png)

Filmy można filtrować ze względu na ocenę, gatunek, producenta i reżysera. Przykład dla filmów Musical - ich id ma wartość 8.

![alt text](https://i.imgur.com/kMD5PC3.png)