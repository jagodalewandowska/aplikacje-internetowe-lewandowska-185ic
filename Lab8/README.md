# Lab 8 - Czat z użyciem Web Socket + Web Workers

####
##### Wymagania dotyczące ósmego zadania:
####

![](https://i.imgur.com/p75NGzC.png) 

---

### Spis treści:

1. [Socket.io]()
2. [WebWorkers]()

---

# Socket.io - czat

[...]

# WebWorkers

WebWrokers pozwalają na wykonywanie skryptów JavaScript w tle, równoległe do głównego wątku. Dzięki temu nie obciążają głównego interfejsu użytkownika. Podczas implementacji tworzony jest nowy obiekt Worker, a także utworzenie odbierania `onmessage` i wysyłania `postmessage` wiadomości między skryptem uruchomionym "w tle". Aby uruchomić WebWorkera należy utworzyć serwer, w moim przypadku za pomocą polecenia 
```
python -m http.server
```

Dla przykładu zostały utworzone dwie funkcje dla **ciągu Fibonacciego** oraz dla obliczania **silni**.

![](https://i.imgur.com/LDjCul4.png)

### Ciąg Fibonacciego

Wywołanie funkcji `startWorkerFib()` odbywa się za pomocą przycisku "Wyświetl". Następuje przejście do skryptu.

![](https://i.imgur.com/jWP6nfR.png)

Funkcja startWorkerFib() zawiera tworzenie nowych zmiennych, z czego jedna odnosi się do elementu "num" będącym polem input. Pobierana wartość przekazywana jest do workera utworzonego za pomocą pliku **fibonacci.js**. Wynik operacji wstawiany jest w miejsce "result". W przypadku, kiedy przeglądarka nie obsługuje workerów zostaje wyświetlony odpowiedni komunikat znajdujący się w `else`. 

![](https://i.imgur.com/vY2FG2u.png)
 
Sam skrypt wykonujący tworzenie ciągu Fibonacciego wygląda następująco. Jeśli wartość wpisana jest większa od zera to wykonywane są standardowe obliczenia - dla wartości 1 oraz 0 wyświetlane są te wartości za pomocą `postMessage(e.data)`, gdzie e.data to przekazana liczba w input. 

Wartości przekazywane są do utworzonej tablicy wraz ze spacją (w celu wyświetlenia ich w polu card wraz z zawijaniem) - 
`arr.push(" " + y)`. Kiedy liczba jest mniejsza od zera wyświetlany jest odpowiedni  komunikat.

![](https://i.imgur.com/7dUUG7T.png)
 
Wykonywanie obliczeń na stronie:

1. #### Dla liczby 1

![](https://i.imgur.com/gQkEKdl.png)

2. #### Dla liczby 24

![](https://i.imgur.com/nRlEf8V.png)

3. #### Dla liczby mniejszej od zera

![](https://i.imgur.com/V6eRzH3.png)

4. #### Dla większej liczby - 100

![](https://i.imgur.com/HXoxOkM.png)
 
 
 
 
 
 
 
 
 
 
 
 