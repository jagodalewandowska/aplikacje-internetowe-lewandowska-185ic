# Lab 8 - Czat z użyciem Web Socket + Web Workers

####
##### Wymagania dotyczące ósmego zadania:
####

![](https://i.imgur.com/p75NGzC.png) 

---

### Spis treści:

1. [Socket.io](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab8#socketio---czat)
	- [index.js](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab8#indexjs)
	- [chat.js](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab8#chatjs)
	- [strona czatu](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab8#strona-czatu)
2. [WebWorkers](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab8#webworkers)
	- [Ciąg Fibonacciego](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab8#ci%C4%85g-fibonacciego)
		- [Wykonywanie obliczeń](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab8#wykonywanie-oblicze%C5%84-na-stronie)
	- [Silnia](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab8#silnia)
		- [Wykonywanie obliczeń](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab8#wykonywanie-oblicze%C5%84-na-stronie)

---

# Socket.io - czat

Socket.IO jest biblioteką JavaScript dla aplikacji webowych. Pozwala na komunikację w czasie rzeczywistym między serwerem i klientami. Posiada dwie strony - klienta, która działa w przeglądarce oraz stronę serwerową dla Node.js. Mają bardzo zbliżone do siebie API.

### index.js

W pliku **index.js** definiowane są zmienne jak express, app, path, http, aby pozwolić na nawiązywanie połączenia. Importowane są pliki statyczne. Dodaną modyfikacją są nazwy użytkowników - dlatego na początku po wejściu na stronę domyślnie użytkownik nie jest 'zalogowany'.
```
let addedUser = false;
```
Tworzenie **nowego** użytkownika wraz ze zmianą statusu addedUser.
```
socket.on('add user', (username) => {
  if (addedUser) return;
  // Przypisanie nicku i zmiana statusu
  socket.username = username;
  addedUser = true;
  socket.emit('login');
});
```
Tworzenie **nowej wiadomości** wraz z przypisywaniem nicku za pomocą funkcji broadcast.
```
socket.on('chat message', (data) => {      
  socket.broadcast.emit('chat message', {
    username: socket.username,
    message: data
  });
});
```
Aby możliwe było wyświetlanie informacji o tym, że któryś z użytkowników pisze wiadomość (is typing) dodany jest fragment kodu, przypisujący nick do osoby która pisze wiadomość.
```
socket.on('typing', () => {
  socket.broadcast.emit('typing', {
  	username: socket.username
  });
});
```
W przypadku kiedy osoba przestaje pisać wiadomość:
```
// Kiedy przestaje pisać dany użytkownik informacja znika
    socket.on('stop typing', () => {
      socket.broadcast.emit('stop typing', {
        username: socket.username
      });
    });
  });
```

### chat.js

Utworzenie stałych przechowujących dane takie jak username, wiadomości, strona loginu, czatu, definiowanie socketa. Na samym początku wartości connected oraz typing na `false`, które będą zmieniane w zależności od działania użytkownika dołączającego do czatu. W zdefiniowanej tablicy `COLORS` znajdują się kolory, które będą losowo generowane dla każdego użytkownika - jest to pula.

![](https://i.imgur.com/pAqEIY0.png)

Ustawianie nazwy użytkownika - jeśli dodany jest nowy nick, to strona logowania zostaje schowana, a wyświetla się okno czatu. Dodanie użytkownika.

![](https://i.imgur.com/H9KeU8l.png)

Losowy kolor dla użytkownika, tworzone za pomocą zmiennej hash, w której z puli kolorów zadeklarowanych wcześniej będą przypisywane kolory dla użytkownika.

![](https://i.imgur.com/QnUumE3.png)

Wysyłanie wiadomości na czacie:

![](https://i.imgur.com/Rm1V3di.png)

Funkcja `addChatMessage`, w której do listy poprzednich wiadomości dodawany jest w nowej linii wiadomość. Tak samo jeśli chodzi o informację o pisaniu wiadomości.

![](https://i.imgur.com/6saRjQm.png)

Dodawanie wiadomości wraz z elementem auto-scrollowania. W przypadku kiedy wiadomości wychodzą poza obszar dokumentu przesuwane są one do góry.

![](https://i.imgur.com/8MArP2m.png)

Wyświetlanie i usuwanie powiadomienia, że użytkownik pisze wiadomość.

![](https://i.imgur.com/qi0L9aR.png)

Zwracanie wiadomości o tym, kto pisze wiadomość w tym momencie.
```
const getTypingMessages = (data) => {
      return $('.typing.message').filter(function (i) {
        return $(this).data('username') === data.username;
      });
    }
```

W przypadku, kiedy użytkownik wciśnie przycisk enter wysyłana jest wiadomość - jeśli jest 'zalogowany'.
![](https://i.imgur.com/xgEqWry.png)

Pozostałe wywołania kodu konieczne do dodawania wiadomości, czy 'animacji' pisania. W przypadku zapisanego użytkownika jest to zmiana jego statusu na połączony - connected.
```
socket.on('login', (data) => {
	connected = true;
});

socket.on('chat message', (data) => {
	addChatMessage(data);
});

socket.on('typing', (data) => {
	addChatTyping(data);
});

socket.on('stop typing', (data) => {
	removeChatTyping(data);
}); 
```

### Strona czatu

Samo wyświetlanie strony znajduje się w pliku *index.html*. Zawiera on nagłówek jak i ekran wpisywania swojego nicku, po przejściu do czatu ten ekran jest 'chowany' a następnie wyświetlany jest 'chatArea'.

![](https://i.imgur.com/RRgcvoP.png)

W jednym z okien loguję się swoim imieniem, w drugim zaraz zaloguję się jako inny użytkownik.

![](https://i.imgur.com/E19sQDx.png)

Wpisując coś na czacie w oknie 'Jagoda' na drugim można zauważyć, że jest pisana wiadomość:

![](https://i.imgur.com/PUOUVZX.png)

![](https://i.imgur.com/lpLujHM.png)

Tak samo działa to w drugą stronę:

![](https://i.imgur.com/OB3vuCy.png)

Za pomocą modyfikacji w css co druga wiadomość ma inny kolor tła (nieparzysta wiadomość). Animacja:

![](https://i.imgur.com/gFSMZqz.gif)

# WebWorkers

WebWorkers pozwalają na wykonywanie skryptów JavaScript w tle, równoległe do głównego wątku. Dzięki temu nie obciążają głównego interfejsu użytkownika. Podczas implementacji tworzony jest nowy obiekt Worker, a także utworzenie odbierania `onmessage` i wysyłania `postmessage` wiadomości między skryptem uruchomionym "w tle". Aby uruchomić WebWorkera należy utworzyć serwer, w moim przypadku za pomocą polecenia 
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