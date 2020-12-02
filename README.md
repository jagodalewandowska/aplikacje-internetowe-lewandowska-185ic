### Aplikacje internetowe
#### Autor: Jagoda Lewandowska, Grupa 185IC


---

### Lab 1 - Blog uruchomiony na PaaS - [Tutaj.](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab1)  
#### Link do bloga: https://blog-lewandowska.herokuapp.com/  

<details>
<summary>Szczegóły</summary>

# Lab 1

## Link do bloga: https://blog-lewandowska.herokuapp.com/  
#### Do utworzenia bloga użyłam Django, a następnie został on umieszczony na platfomie Heroku. 


---
####
##### Wymagania dotyczące pierwszego zadania:
####

![alt text](https://i.imgur.com/5amOJqU.png)

# Zrzuty ekranów poszczególnych stron

### Strona główna
##### Strona główna bloga zawiera wpisy. W przypadku bycia niezalogowanym, przycisk w górnym rogu nie jest widoczny.
####

- Przed zalogowaniem:
![alt text](https://i.imgur.com/8sMBGNC.png)  

- Po zalogowaniu:
![alt text](https://i.imgur.com/j59VJR0.png)


---
### Edycja postów i usuwanie
##### Po kliknięciu na tytuł posta następuje przejście do edycji. Strona zawiera dwa przyciski, które służą do edycji a także usuwania.
####

![alt text](https://i.imgur.com/W8y8A9J.png)  


---
### Ekran dodawania nowego posta
##### Jeśli użytkownik jest zalogowany pod adresem https://blog-lewandowska.herokuapp.com//admin, możliwe jest dodawanie postów w prawym górnym rogu strony.

![alt text](https://i.imgur.com/xFLBCE0.png)  

- Dodanie nowego posta

![alt text](https://i.imgur.com/13VmDoc.png)  

Post widnieje na blogu:  

![alt text](https://i.imgur.com/5IsfFRB.png)  

Po wciśnięciu na nagłówek wpisu i kliknięcie przycisku usunięcie:

![alt text](https://i.imgur.com/1m9gr11.png)  



---
### Panel administratora
##### Po zalogowaniu możliwe jest dodawanie postów, czy sprawdzanie historii edycji postów.  

![alt text](https://i.imgur.com/P4EFERL.png)  
![alt text](https://i.imgur.com/spvRRMp.png)


---
</details>


---

### Lab 2 - Rejestracja użytkowników - [Tutaj.](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab2) 
#### Link do strony: https://auth-lewandowska.herokuapp.com/   

<details>
<summary>Szczegóły</summary>

# Lab 2

## Link do strony: https://auth-lewandowska.herokuapp.com/  
#### Do utworzenia strony użyłam Django, a następnie został on umieszczony na platfomie Heroku. 


---
####
##### Wymagania dotyczące pierwszego zadania:
####

![alt text](https://i.imgur.com/fx3svD2.png)

# Zrzuty ekranów poszczególnych stron

## Strona główna
##### Strona główna zawiera poniższy widok, w zależności, czy użytkownik jest lub nie jest zalogowany. Jest również pasek nawigacji, z którego można przejść do mojego Githuba.
####

Zrzut ekranu w przypadku niezalogowanego użytkownika:
![alt text](https://i.imgur.com/xVmI5qg.png)  



---
## Rejestracja użytkownika
##### Po kliknięciu na przycisk zarejestruj się widnieje następujące okno. Tworzę użytkownika **Jagoda**:
####

![alt text](https://i.imgur.com/JF8pC07.png)  


---
## Logowanie
##### Przeniesienie do ekranu logowania - wpisuję dane:
####

![alt text](https://i.imgur.com/wqLQAhT.png)  



---
## Ekran zalogowanego użytkownika
##### Na stronie głównej możliwe jest teraz wylogowanie się, a także zmiana hasła. 

![alt text](https://i.imgur.com/LRrEygV.png)


---
## Zmiana hasła
##### Należy podać stare hasło, a następnie dwukrotnie nowe. 

![alt text](https://i.imgur.com/Mt7nWKM.png)  

#### Po zmianie hasła widnieje następujące okno:

![alt text](https://i.imgur.com/chv3suk.png)

#### Przenoszę się do stony głównej, z której mogę się wylogować.

---
### Resetowanie hasła
##### Na stronie podaję adres e-mail.

![alt text](https://i.imgur.com/Vt4jBst.png)  

##### Otrzymuję link do resetowania hasła w konsoli:

![alt text](https://i.imgur.com/JxCuRv5.png)  

##### Podaję nowe hasło oraz je potwierdzam.

![alt text](https://i.imgur.com/QGG02L9.png)  

##### Po zatwierdzeniu widoczne okno, z którego można przejść do logowania.

![alt text](https://i.imgur.com/BY7Z7E3.png)

</details>  


---

### Lab 3 - Różne sposoby uwierzytelniania - [Tutaj.](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab3)  
#### Link do strony: https://social-lewandowska.herokuapp.com/

<details>
<summary>Szczegóły</summary>

# Lab 3

## Link do strony: https://social-lewandowska.herokuapp.com/ 
#### Do utworzenia strony użyłam Django, a następnie został on umieszczony na platfomie Heroku. 


---
####
##### Wymagania dotyczące pierwszego zadania:
####

![alt text](https://i.imgur.com/WAgSdJb.png)

# Zrzuty ekranów poszczególnych stron

## Strona główna - Localhost

##### Strona główna zawiera poniższy widok, w zależności, czy użytkownik jest lub nie jest zalogowany. Jest również pasek nawigacji, z którego można przejść do mojego Githuba. Do zadania 3 dodane zostały przyciski rejestracji za pomocą e-mail, a także Githuba oraz Facebook. W drugiej części pliku Readme znajdują się zrzuty ekranu w przypadku dodania na Heroku.
####

Zrzut ekranu w przypadku niezalogowanego użytkownika:
![alt text](https://i.imgur.com/5kNSvBh.png)  



---
## Rejestracja użytkownika za pomocą adresu e-mail
##### Po kliknięciu na przycisk zarejestruj się widnieje następujące okno. Tworzę użytkownika **JagodaTest wraz z adresem e-mail**:
####

![alt text](https://i.imgur.com/gDeckDs.png)  


---
## Ekran po poprawnej rejestracji
##### Możliwość przejścia do ekranu logowania
####

![alt text](https://i.imgur.com/1c5DzDT.png)  



---
## Ekran logowania
##### Logowanie za pomocą utworzonego użytkownika

![alt text](https://i.imgur.com/0qBexoO.png)


---
## Ekran główny po zalogowaniu się nowego użytkownika
##### Możliwość zmiany hasła oraz wylogowania się

![alt text](https://i.imgur.com/tHFFeGX.png)  


---
### Logowanie za pomocą Facebook
##### Przycisk Sign in with Facebook

![alt text](https://i.imgur.com/muSB8Hv.png)  

##### Po zalogowaniu:

![alt text](https://i.imgur.com/49gpdQD.png)  


---
### Logowanie za pomocą Github
##### Przycisk Sign in with Github

![alt text](https://i.imgur.com/aSYRTXg.png)  

##### Po zalogowaniu:

![alt text](https://i.imgur.com/eel3sQj.png)  


---
### Widok nowych użytkowników w panelu administratora
##### Użytkownicy dodani za pomocą adresu e-mail, github oraz facebook

![alt text](https://i.imgur.com/yFKFuZ7.png)  


---
---

# Po dodaniu na Heroku


### Strona główna
![alt text](https://i.imgur.com/6BWNsHj.png)  


### Tworzenie użytkownika
![alt text](https://i.imgur.com/jtTOTfI.png)  


### Rejestracja pomyślna
![alt text](https://i.imgur.com/fAtBo5r.png)    


### Logowanie się nowego użytkownika
![alt text](https://i.imgur.com/HMi2LC7.png)    


### Ekran po zalogowaniu
![alt text](https://i.imgur.com/xNmSyZM.png)    


### Logowanie przez **Github**
![alt text](https://i.imgur.com/ztMO7nc.png)    


### Po zalogowaniu
![alt text](https://i.imgur.com/r38Nlpw.png)    


### Logowanie przez **Facebook**
![alt text](https://i.imgur.com/gkYFMlR.png)    


### Po zalogowaniu
![alt text](https://i.imgur.com/Co98n4B.png)  


### W panelu administratora, kolejno:

- administrator
- konto github
- konto facebook
- konto założone poprzez adres e-mail

![alt text](https://i.imgur.com/vwbnVUu.png)


</details>  


---

### Lab 4 - REST API z DRF - [Tutaj.](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab4)  

<details>
<summary>Szczegóły</summary>

# Lab 4

Wykorzystanie Django REST Framework. Dodanie Swaggera.

####
##### Wymagania dotyczące czwartego zadania:
####

![alt text](https://i.imgur.com/TwbYQN0.png)  


---
# Realizacja kodu z zajeć wraz z małymi modyfikacjami

Jedną z dwóch utworzonych aplikacji w projekcie to posts. Do analizy rozpoczynam od PostList. To tutaj widnieją wszystkie posty, a także jest możliwe dodawanie nowych. Jeśli użytkownik jest niezalogowany nie są wyświetlane żadne z istniejących elementów. Podląg dodanych postów w panelu administratora:

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

</details>


---

### Lab 5 - Web Scraping - [Tutaj.]()  

<details>
<summary>Szczegóły</summary>
</details>


---

### Lab 6 - Bezpieczeństwo w Django - [Tutaj.]()  

<details>
<summary>Szczegóły</summary>
</details>


---

### Lab 7 - Zadania asynchroniczne z Celery - [Tutaj.]()  

<details>
<summary>Szczegóły</summary>
</details>


---

### Lab 8 - Czat z użyciem django-channels - [Tutaj.]()  

<details>
<summary>Szczegóły</summary>
</details>


---

### Lab 9 -  Django + Redis - [Tutaj.]()  

<details>
<summary>Szczegóły</summary>
</details>


---

### Lab 10 - Django + React - [Tutaj.]()  

<details>
<summary>Szczegóły</summary>
</details>