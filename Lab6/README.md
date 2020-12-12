# Lab 6 - kontynuacja Lab 4

Wykorzystanie Django REST Framework. Viewsets, basic, token, session, implementacja licznika cookies.

####
##### Wymagania dotyczące szóstego zadania:
####

![alt text](https://i.imgur.com/AT3WlNO.png)  


---
# Realizacja kodu z zajeć wraz z małymi modyfikacjami

Aplikacje w projekcie do kontynuacja lab4. Są tutaj dwie aplikacje: 
- **Posts** - /api/v1
- **Movies** - /api/v2

## Viewsets 

### 1. Posts

Obiekty typu ViewSet nie posiadają metod takich jak get() czy post(), ale posiadają list() oraz create(). Dzięki temu można zastosować Routers w następnym podpunkcie.

![alt text](https://i.imgur.com/XGGDUvA.png)


**Serializery** - dzięki nim można wybrać jakie elementy są wyświetlanie na stronie. Zmodyfikowałam je tak, aby wyświetlane były również adresy email:

![alt text](https://i.imgur.com/5LZhkdL.png)

Wyświetlanie wszystkich użytkowników:

![alt text](https://i.imgur.com/34M1cAB.png)

Później można użyć ten ViewSet tworząc Routers.


### 2. Movies

Viewset jaki stworzyłam dla nowej aplikacji to ten wyświetlający listę filmów o nazwie MovieViewSet. Obiekty typu ViewSet nie posiadają metod takich jak get() czy post(), ale posiadają list() oraz create().

![alt text](https://i.imgur.com/wHkCdz1.png)

Dzięki temu wykorzystałam w późniejszym kroku ten widok w tworzeniu routers:

```
...
router = SimpleRouter()
router.register('', MovieViewSet, basename='movieset')

urlpatterns += router.urls
...
```

##### Serializery - Wyświetlane są wszystkie atrybuty:

![alt text](https://i.imgur.com/foHzCn7.png)

Można by było zastosować formę exclude i usuwając np. producer z listy nie byłby już on wyświetlany.


## Routers

### 1. Posts - dla postów
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

### 2. Posts - dla użytkowników

W tym laboratorium dodane były również nowy ViewSet dla użytkowników. Dlatego też, w posts/urls.py dodałam następujacą linię:

```
...
      # od teraz zamist user details jest user instance - dodatkowa opcja usuwania
      router.register('users', UserViewSet, basename='users')
															...
```
Url pozostaje puste, jednak jeśli byłoby tam coś zdefiniowane zamieniona byłaby wartość urlpatterns = router.urls na
```
urlpatterns += router.urls
```

Routers działa dla adresu po wpisaniu url **/v1/users/3**:

![alt text](https://i.imgur.com/0Yv0NZz.png)

### 3. Movies

Jak wcześniej wymieniony dla Movies również istnieje Routers:

```
...
router = SimpleRouter()
router.register('', MovieViewSet, basename='movieset')

urlpatterns += router.urls
...
```

## Uwierzytelnianie (basic, session, token)

By móc korzystać z nowego typu uwierzytelniania konieczne było dodanie fragmentu kody do settings.py. Są to domyślne klasy to utwierzytelniania:
```
'DEFAULT_AUTHENTICATION_CLASSES': [
'rest_framework.authentication.SessionAuthentication',
#'rest_framework.authentication.BasicAuthentication',
'rest_framework.authentication.TokenAuthentication',
],
```
Gdzie sessions jest wciąż potrzebne dla przeglądania API, ale Tokeny będą wykorzystywane do przekazywania danych w nagłówku HTTP. Kolejną rzeczą do doania są "'rest_framework.authtoken'," w zainstalowanych aplikacjach. Podgląd tokenów w panelu administratora, które dodane są tylko dla użytkowników ktorzy zalogowali się po dodawaniu tokenów do strony. Znajduje się on pod adresem **/admin/authtoken/tokenproxy/**.

![alt text](https://i.imgur.com/ToUB3o2.png)

Widoki:

1. #### **Login** /rest-auth/login

![alt text](https://i.imgur.com/NmjYAMH.png)

2. #### **Logout** /rest-auth/reset

![alt text](https://i.imgur.com/fLAjsdc.png)

3. #### **Password Reset** - /rest-auth/password/reset

![alt text](https://i.imgur.com/LdeBiIn.png)

4. #### **Password Reset Confirm** - /rest-auth/password/reset/confirm

![alt text](https://i.imgur.com/4vFWuoe.png)

5. #### **Register** - /rest-auth/registration

![alt text](https://i.imgur.com/xMP60tf.png)

Wynik rejestracji:

![alt text](https://i.imgur.com/wIUswHa.png)

Otrzymany email:

![alt text](https://i.imgur.com/Jpw4K2U.png)

Nowy token:

![alt text](https://i.imgur.com/3b9NfEi.png)



## Licznik wizyt z użyciem Cookies

Aby utworzyć prosty licznik wejść zdefiniowalam nową funkcję w posts/views.py. Wyświetla ona proste powiadomienie w przypadku wejścia na stronę główną, przekierowanie znajduje się w urls.py:
```
urlpatterns = [
   path('', cookies, name='home'),     
   			...
```
Gdzie **cookies** jest moją nową funkcją. Wygląda ona następująco:

![alt text](https://i.imgur.com/7ADPsjd.png)

Na początku definiowana jest wartość html, a następnie zastosowana jest prosty if, który w zależzności, jeśli znajdzie wartość cookies dla nas wyświetlana jest wiadomość, że jesteśmy na stronie po raz pierwszy, jeśli nie, jest informacja, który to raz na stronie.

- ### **Pierwszy raz**

![alt text](https://i.imgur.com/JQQCJf1.png)

- ### **Piąty raz**

![alt text](https://i.imgur.com/vWgpktJ.png)

- ### **Animacja**

![alt text](https://i.imgur.com/ul9CtdB.gif)


---


# Własna aplikacja Movies - Filtry i Sortowanie

Dla postow filtrowanie zostało również zaimplementowane, jednak teraz pokażę filtrowanie dla filmów z poprzedniego laboratorium (Lab4) oraz dodawanie gatunków.
Aplikacja zawiera Obiekty Genre - które przy tworzeniu Movies można wykorzystywać z listy, dodając nową pozycję. Stan początkowy to:

![alt text](https://i.imgur.com/GinUapw.png)

A także listę 12 filmów, które mają nadane wartości z obiektu gatunek.

![alt  text](https://i.imgur.com/XpuqKdn.png)

## Dodawanie nowego gatunku oraz filmu

Dodawanie nowego gatunku jako administrator:

![alt text](https://i.imgur.com/V6NByCI.png)

Dodawanie nowego filmu:

![alt text](https://i.imgur.com/smmP2GY.png)




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