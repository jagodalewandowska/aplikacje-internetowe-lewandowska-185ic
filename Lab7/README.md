# Lab 7 - Python + Redis + Django

####
##### Wymagania dotyczące siódmego zadania:
####

![alt text](https://i.imgur.com/DcmZTK8.png)  


---
# **Wykonanie zadań z artykułów**

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

### 5-strumienie

Utworzenie strumienia

![](https://i.imgur.com/g5FUVtw.png)

Wynik

![](https://i.imgur.com/s51R3il.png)

Liczy przed kluczem do identyfikator. Pierwsza wartość do milisekundy od 1 stycznia 1970, a następne to nazwa sekwencji.

### 5a-strumienie-block

![](https://i.imgur.com/EGLX5NC.png)

Dodanie elementu:

![](https://i.imgur.com/iaah5ty.png)


### 5b-strumienie-point

Aby elementy nie ginęły, konieczny jest następujący kod

![](https://i.imgur.com/ljesF5o.png)

Wykorzystanie xdel, które jest jedynym zamiennikiem xack jeśli nie wykorzystywane jest grupowanie konsumentów:
```
redis_connection.xdel(stream_name, msg_id)
```

### 6-pipelining

Obserwowanie kluczy, czy nie zmieniły się za pomocą polecenia **watch**. 

![](https://i.imgur.com/25KT6Uy.png)

nil - oznacza niepowodzenie, ponieważ klucz zmienił się. 

![](https://i.imgur.com/jAlWcBc.png)

### 7-lua

Przekazywanie w komendzie eval ciało skryptu napisanego w lua. Redis odbiera kod, wykonuje i zwraca rezultat. Wyświetlenie słowa test. Drugi argument eval to 0, określa ilość argumentów które można przekazać do skrypti/ Lua ideksuje od 1, wszystko przekazane jest do tabeli argv.

![](https://i.imgur.com/3rXIXi6.png)

![](https://i.imgur.com/jAlWcBc.png)

### 7a-lua-keys

Pierwsze dwa argmenty określane są w tabeli keys, a kolejne w tabeli argv. Skrypt przekazuje dane i zwraca je jako tablicę. 

![](https://i.imgur.com/45r9Sqz.png)

Wynik

![](https://i.imgur.com/JimKNPP.png)


### 7b-lua-array

Utworzenie tablicy 15 elementowej

![](https://i.imgur.com/PdEJGZj.png)

Wyświetlenie elementów:

![](https://i.imgur.com/yu1LHVP.png)

### 7c-lua-json

Aby wykorzystywać dane json, wykonanie działania

![](https://i.imgur.com/0rkqwOE.png)

Wynik, liczba 27

![](https://i.imgur.com/KPwpnRi.png)

### 7d-lua-call

Dodanie wartości 11 i 5 w przykładzie z artykułu:

![](https://i.imgur.com/eohrjmV.png)

Wynik

![](https://i.imgur.com/EzatrNA.png)

### 7e-lua-another

![](https://i.imgur.com/ZwlNTVN.png)

### 7f-lua-cache

![](https://i.imgur.com/kOg9zQS.png)

### 8-not

Nasłuchiwanie każdej zmiany klucza. Następujący kod wraz z uruchomieniem:

![](https://i.imgur.com/BzHa695.png)

Zmiany:

![](https://i.imgur.com/GzH5QYI.png)

Po wykonaniu nowego polecenia o treści append

![](https://i.imgur.com/xr2WRVm.png)

### 8-keyevent

Powiadomienia o każdym użyciu komendy set.

![](https://i.imgur.com/FLT6jQ0.png)


# **Django-Redis-Celery**

Zainstalowanie i włączenie **redis_server.exe**.

![](https://i.imgur.com/POIkkGK.png)

redis_cli.exe również działa:

![](https://i.imgur.com/0txcYye.png)

Test:

![](https://i.imgur.com/P19VFOy.png)

Utworzenie pliku celery.py w nowym projekcie, który zawiera powiązanie środowiska projektu a celery tak, aby sam wykyrwał w nim zadania do obsłużenia.

Tworzony jest instancji klasy Celery:
```
celery_app = Celery('image_parroter')
```
A następnie aktualizowanie konfiguracji tak, aby wykrywane były zadania w projekcie - a konfiguracje zaczynają się od CELERY_.

Dodanie nowych aplikacji w settings:

![](https://i.imgur.com/rCuk3WT.png)

Następnie na dole ustawień konieczne jest dodanie lokalizacji, jeśli nie istnieją. Są to media_root oraz images_dir:
```
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
IMAGES_DIR = os.path.join(MEDIA_ROOT, 'images')
```

Trzeba również zaznaczyć jaki jest dumyslny adres, jego backend, jaki format będzie akceptowalny:
```
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
```

W utworzonym pliku **tasks.py** konieczny jest import narzędzia do zarządzania plikami zip: tak jak odczytywanie, zapisywanie. Tworzone są zadania w @shared_task - która akceptuje wymiary obrazu tworząc nowy. Na początku jest to rozdzielanie ścieżek oraz zdefiniowanie miejsca przechowywania danych i jak wyglądać będzie zwracanie url końcowego.

![](https://i.imgur.com/X3b7cZy.png)

Następnie jest próba otwarcia obrazu i przy wykorzystaniu zaimportowanych elementów zapisywanie nowych elementów i kopiowanie starych - oryginalnnych.

![](https://i.imgur.com/RHS9GB4.png)

W **views.py** utworzone są różne elementy:

- FileUploadForm - formularz do przesyłania elementów
- HomeView - do wyświetlania głównej strony, który jednocześnie wykorzystuje obiekt FileUploadForm oraz pole ImageField
- TaskView - sprawdzanie statusu make_thumbnails, wykorzystywane przez AJAX

Fragment HomeView, tworzącego nowy obiekt i ewentualne zwracanie formularza w przypadku błędów.

![](https://i.imgur.com/xtRhpTd.png)

W TaskView:

![](https://i.imgur.com/EuePph9.png)

Strona, dodanie elementu:

![](https://i.imgur.com/6HT9IFz.png)

Otrzymany plik zip:

![](https://i.imgur.com/BHuueJt.png)

Konsola celery:

![](https://i.imgur.com/hJlxZJR.png)

Odpowiedź:

![](https://i.imgur.com/RDhMnAf.png)

![](https://i.imgur.com/hNx5rT0.png)

# Workery, własne taski

Pierwszy task to mnożenie i dzielenie:

![](https://i.imgur.com/vAHkK23.png)

Widać je podczas uruchamiania w konsoli:

![](https://i.imgur.com/hJsodp4.png)

Po przejściu do shell importuję task:

![](https://i.imgur.com/Y1MbZEY.png)

A następnie wykorzystując import i wykorzystując polecenie get otrzymuję wynik:

![](https://i.imgur.com/W0Fmlwg.png)

Tak samo dla dzielenia:

![](https://i.imgur.com/J4lpZ09.png)

















