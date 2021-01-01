# Lab 7 - Python + Redis + Django

####
##### Wymagania dotyczące siódmego zadania:
####

![alt text](https://i.imgur.com/DcmZTK8.png)  


---
# Wykonanie zadań z artykułów

## Artykuł 1 - instalacja, połaczenie z redis, redis-cli

![alt text](https://i.imgur.com/lE3O7SK.png)

### 1.1-connection

Sprawdzenie połączenia z redis:

![alt text](https://i.imgur.com/EQatqmJ.png)  

Wartość **True** w odpowiedzi na uruchomienie kodu:

![alt text](https://i.imgur.com/5OzAnkb.png)

Redis-cli

![alt text](https://i.imgur.com/iLbWPMK.png)  

### 1.2-key-1

Przypisanie wartości:

![alt text](https://i.imgur.com/nVhvLEH.png)  

Wynik:

![alt text](https://i.imgur.com/THZUdFD.png)  

### 1.2-key-2

Dodanie wartości decode-responses, dzięki czemu nie pojawia się już fragment
```
b'...'
```
![alt text](https://i.imgur.com/P84KHDm.png)

Odpowiedź:

![alt text](https://i.imgur.com/nMjUnBM.png)  

Dostanie się do wartości poprzez redis-cli:

![alt text](https://i.imgur.com/l9LbNZS.png)

### 1.2-key-3

Append, delete

![alt text](https://i.imgur.com/7rtRGj2.png)

Wynik:

![alt text](https://i.imgur.com/RXOcapi.png)

### 1.2-key-4

Dodanie i odejmowanie wartości

![alt text](https://i.imgur.com/v8gqwO2.png)

Wynik:

![al text](https://i.imgur.com/LN7ateh.png)

## Artykuł 2 - Listy

### 2-listy

![](https://i.imgur.com/CRr9mc4.png)

Wyświetlenie:

![](https://i.imgur.com/OvHQSPV.png)

Zwrócenie innych wartości:

![](https://i.imgur.com/guniEgJ.png)

Wynik:

![](https://i.imgur.com/Scr4Caz.png)

### 2a-listy-br

Wyświetlenie programu, który działa cały czas, brpop jest blokada programu, jesli na liście nie będzie elementu. W przeciwnym przypadku zapętla się, pobierając elementy i kończąc program.

![](https://i.imgur.com/aKQoWea.png)

Wynik:

![](https://i.imgur.com/O3wCyK9.png)

### 2b-listy-select

Select służy do przełączania się między przestrzeniami. Polega to na tym, że dana zostaje zapisana na bazie zerowej, a następnie odczytywana jest z pierwszej by otrzymać poprawną wartość - 'wartosc'

![](https://i.imgur.com/nLrkd41.png)

Wynik:

![](https://i.imgur.com/LfVfAGI.png)

### 2c-listy-ttl

Ustawienia "życia" klucza na 24. Po tym czasie jest usuwany.

![](https://i.imgur.com/zfB9XzK.png)

Wynik:

![](https://i.imgur.com/yOe34ai.png)

### 2d-listy-set-expire

Odpowiednik poprzedniego, z użyciem poleceń set oraz expire

![](https://i.imgur.com/renuXTt.png)

Wynik:

![](https://i.imgur.com/MCsXCUm.png)

### 3-zbiory

Utworzenie zbioru. Za każdym razem wyświetlane są inne elementy:

![](https://i.imgur.com/X1rla8J.png)

Uruchomienie programu 3 razy, za każdym razem elementy wyświetlone są w innej kolejności:

![](https://i.imgur.com/jfQfZct.png)

### 3a-posortowane-zbiory

Stworzenie klucze, które będą posortowane według przypisanych wartości.

![](https://i.imgur.com/4WKfQHT.png)

Wyświetlenie kluczy:

![](https://i.imgur.com/iESiLsk.png)

### 3b-posortowane-zbiory-modyfikacje

Wartości w różnych kolejnościach, powinny być wyświetlone klucz2 -> klucz4 -> klucz3 -> klucz1.

![](https://i.imgur.com/s4bmrqR.png)

Wyświetlenie

![](https://i.imgur.com/748cnCB.png)

### 3c-posortowane-zbiory-same

W przypadku takich samych wartości dodanie withscores, by pokazać że mają one takie same wartości.

![](https://i.imgur.com/G4DJ7YL.png)

Wyniki

![](https://i.imgur.com/Xp6Zc82.png)

### 3d-hash
Wykorzystanie hash - czyli map, słowników.

![](https://i.imgur.com/TsDGwsa.png)

Wynik:

![](https://i.imgur.com/QpVnufi.png)


### 4-pubsub

Utworzenie subskrybenta z kluczem **test**.

![](https://i.imgur.com/cJ8iYaj.png)

Wynik

![](https://i.imgur.com/zxaJ2WR.png)

Utworzenie nowej wiadomości

![](https://i.imgur.com/xpFRr5Y.png)

Ponieważ wcześniej uruchomiony pubsub oczekuje na nowe wiadomości, wyświetlona zostaje nowa wiadomość:

![](https://i.imgur.com/n4XxSCX.png)

### 4-pubsub-task

Podłączanie się do kanałów

![](https://i.imgur.com/1pnvMHK.png)

Wynik

![](https://i.imgur.com/L6KgoaA.png)























