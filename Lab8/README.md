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

## Ciąg Fibonacciego

Wywołanie funkcji `startWorkerFib()` odbywa się za pomocą przycisku "Wyświetl". Następuje przejście do skryptu.

![](https://i.imgur.com/qS25340.png)

Funkcja startWorkerFib() zawiera tworzenie nowych zmiennych, z czego jedna odnosi się do elementu "num" będącym polem input. Pobierana wartość przekazywana jest do workera utworzonego za pomocą pliku **fibonacci.js**. Wynik operacji wstawiany jest w miejsce "result". W przypadku, kiedy przeglądarka nie obsługuje workerów zostaje wyświetlony odpowiedni komunikat znajdujący się w `else`. 

![](https://i.imgur.com/vY2FG2u.png)
 
Sam skrypt wykonujący tworzenie ciągu Fibonacciego wygląda następująco. Jeśli wartość wpisana jest większa od zera to wykonywane są standardowe obliczenia - dla wartości 1 oraz 0 wyświetlane są te wartości za pomocą `postMessage(e.data)`, gdzie e.data to przekazana liczba w input. 

Wartości przekazywane są do utworzonej tablicy wraz ze spacją (w celu wyświetlenia ich w polu card wraz z zawijaniem) - 
`arr.push(" " + y)`. Kiedy liczba jest mniejsza od zera wyświetlany jest odpowiedni  komunikat.

![](https://i.imgur.com/uOA8VKL.png)
 
### Wykonywanie obliczeń na stronie:

1. Dla liczby 1

![](https://i.imgur.com/gQkEKdl.png)

2. Dla liczby 24

![](https://i.imgur.com/nRlEf8V.png)

3. Dla liczby mniejszej od zera

![](https://i.imgur.com/o1NPz4A.png)

4. #### Dla większej liczby - 100

![](https://i.imgur.com/HXoxOkM.png)
 
## Silnia

Tak samo jak w poprzednim przykładzie obliczanie wartości następuje po wciśnięciu przycisku *wyświetl*. Wywoływana jest funkcja `startWorkerExp()`.

![](https://i.imgur.com/hEffrFh.png)

Funkcja startWorkerExp() wygląda bardzo podobnie do poprzedniej, tym razem wartość przekazywana będzie pod `'id=num2
'`. Tak samo utworzony jest nowy obiekt Worker, wykorzystywany jest utworzony plik ze skryptem, tym razem jest to `exp.js`. Wynik wyświetlany jest w polu `resultExp`.

![](https://i.imgur.com/wsnz3aL.png)

Wzór na silnię to:
```
											n!=1⋅2⋅3⋅...⋅(n−1)⋅n
```

Obliczanie silni to prosty kod zawierający pętlę. 

![](https://i.imgur.com/ORsSvs2.png)

### Wykonywanie obliczeń

1. Dla liczby 1

![](https://i.imgur.com/KbBRk3c.png)

2. Dla liczby 12

![](https://i.imgur.com/yM5y8vg.png)
 
3. Dla liczby 100

![](https://i.imgur.com/Av0h9ph.png)

4. Dla liczby ujemnej

![](https://i.imgur.com/xJLVf2Z.png)

 
 
 
 
 