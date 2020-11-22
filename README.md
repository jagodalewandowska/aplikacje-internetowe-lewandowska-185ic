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

### Lab 3 - REST API z DRF [Tutaj.](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab3)  

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

### Lab 4 - Social website - part 1 - [Tutaj.]()  

<details>
<summary>Szczegóły</summary>
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