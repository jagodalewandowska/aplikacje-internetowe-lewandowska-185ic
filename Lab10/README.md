# Lab 10 - Django + React

####
##### Wymagania dotyczące dziesiątego zadania:
####

![alt text](https://i.imgur.com/Exgxj6K.png) 

---

### Spis treści:

1. [Backend](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab10#backend)
2. [Frontend](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab10#frontend)
	- 	Wykorzystane [komponenty](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab10#komponenty)
	- 	Completed/incompleted [tasks](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab10#completed-incompleted-tasks)
	- 	Zarządzanie [postami](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab10#zarz%C4%85dzanie-postami)
		- 	[dodawanie](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab10#dodawanie-posta)
		- 	[usuwanie](https://github.com/jagodalewandowska/aplikacje-internetowe-lewandowska-185ic/tree/main/Lab10#usuwanie-posta)


---
# Backend

Zadaniem było stworzenie aplikacji typu todo. W projekcie django naszą aplikacją jest records - czyli wpisy, dlatego też w **models.py** zostaje utworzony nowy model Record z kilkoma dodatkowymi elementami (oprócz zmiany elementów wizualnych do aplikacji dodane jest również wyświetlanie dnia, czy zmienianie koloru w zależności czy czas na wykonanie minął).

Utworzenie modelu wpisu, który zawiera:
- **tytuł** - max. długość to 200
- **opis** - jako pole tekstowe
- **dodatkowe uwagi** - max. długość również do 200 - miejsce na dodatowy komentarz
- **status** - pole typu true false służace do zmian statusu na ukończone zadanie
- **datę** - do wybierania daty wykonania

![](https://i.imgur.com/OGQ203n.png)

W celu wyświetlania wpisów w profilu administratora dodanie klasy w pliku **admin.py**, która zawiera wszystkie elementy dodane do modelu wcześniej. 

![](https://i.imgur.com/PZwD8Ph.png)

3. Widok w panelu administratora:

![](https://i.imgur.com/8AVWhhy.png)

Ze względu na to, że dodałam wcześniej przykładowe wpisy są one widoczne w zakładce Records.

![](https://i.imgur.com/ySlY31L.png)

W **urls.py** podobnie jak na zajęciach wcześniej utworzone są ścieżki. Wykorzystywane są routers importowane z rest_framework, dzięki którym można generować adresy records/id -- gdzie id to unikalny numer wpisu. Pozostałe ścieżki to tradycyjnie api oraz admin.

![](https://i.imgur.com/iuuzKV8.png)

W widokach znajduje się tylko jeden, definiujący serializer oraz queryset, zawierający wszystkie obiekty modelu Record.
```
class RecordView(viewsets.ModelViewSet):
  serializer_class = RecordSerializer
  queryset = Record.objects.all()  
```

Wykorzystany serializer to **RecordSerializer**, który pozwala na wyświetlanie wszystkich zdefiniowanych parametrów.
```
fields = ('id', 'title', 'description', 'notes', 'finished', 'date')
```
Do "whitelist" zostaje dodany adres **localhost:3000**, na którym znajduje się frontend, blokując wszystkie inne adresy z których mogłby przyjść zapytanie.
```
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
```
Przechodząc pod adres **localhost:8000/api/records** możliwe jest zatem podejrzenie wszystkich dodanych wpisów (które również widoczne są w panelu administratora).

![](https://i.imgur.com/khsLS0p.png)

Dla przykładu dla id numer 8 adresem będzie api/records/8. Po przejściu możliwe jest edytowanie oraz usuwanie tego postu.

![](https://i.imgur.com/26ZkOHj.png)  

---

# Frontend

Wygląd strony:

![](https://i.imgur.com/mpoxrmy.png)

### Komponenty

Dla frontendu utworzyłam 3 komponenty:

1. **Header.js**
2. **Modal.js**
3. **TodayIs.js**

Komponent **Header** zawiera nagłówek, dla którego modyfikacje znajduja się w App.css (wysokość, modyfikacja napisu). Dodanym elementem jest komponent **Typical** dodający tekst z animacją pisania.

![](https://i.imgur.com/miZqxJg.png)

Komponent **Modal** dotyczy wyświetlającego się okienka dodającego nowy wpis. Za pomocą niego można wypełniać poszczególne pola:

![](https://i.imgur.com/WQdUUaE.png)

Komponent **TodayIs** zwraca dzisiejszą datę, pobierając za pomocą funkcji getFullYear, getMonth oraz getDate -- rok, miesiąc, dzień dodając pomiędzy nimi symbol '/'.
```
...
        var today = new Date(),
            date = today.getFullYear() + '/' + (today.getMonth() + 1) + '/' + today.getDate();

            this.state = {
              currentDate: date
            }
          }
          render() {
            return (
              <div>
                <h4> Today is {this.state.currentDate}. </h4>
              </div>
            );
...
```
Wynik wyświetlany jest na stronie ponad panelem z datą.

![](https://i.imgur.com/67pjQ5j.png)

### Completed, incompleted tasks

Wciskając przycisk Completed task następuje wyświetlenie tych ukończonych. Zarówno dla Completed jak i incompleted sprawdzane jest, czy data, która została wyznaczona by dane zadanie ukończyć została przekroczona. Jeśli nie jest, wyświetlone zostaje na **zielono**:
```
Deadline: [data]
```
Dla completed task na ten moment jest tylko jedno, ukończone zadanie na które jest czas do dzisiaj:
![](https://i.imgur.com/z3riL4I.png)

W przeciwnym przypadku jest to informacja na **czerwono**:

![](https://i.imgur.com/mIstuRr.png)

Możliwe jest to dzięki dodanej przeze mnie funkcji jako modyfikacji aplikacji **outDated**, która tworzy nowe obiekty typu Date -- now oraz then:

```
const now = new Date();
const then = new Date(item.date);
```

następnie zeruję godzinę (aby zadanie wciąż było na zielone, jeśli dzisiaj jest ostatni dzień na jego wykonanie). Następnie porównuję te wartości i zwracane jest *true* lub *false*.
```
if (now.getTime() <= then.getTime()) {
      return false;
    } else {
      return true;
    }
```
Wywołuję je w funkcji **renderItems** następującym kodem, sprawdzającym te wartości,
```
{this.outDated(item) ? <b style={{color: 'red'}}>It's past the deadline: {item.date}</b>
            : <b style={{color: 'green'}}>Deadline: {item.date}</b>}
```
w zależności od tego, który przycisk został wciśnięty (w większości przypadków na stronie wykorzystywany jest **bootstrap**).

![](https://i.imgur.com/lLAdjYy.png)

### Zarządzanie postami

1. ##### Dodawanie posta

W tym zadaniu wykorzystywany jest axios w którym za pomocą przypisanego id dodawany jest nowy wpis pod wskazany adres url:
```
...
if (item.id) {
      axios
        .put(`http://localhost:8000/api/records/${item.id}/`, item)
        .then(res => this.refreshList());
      return;
    }
    ...
```
Na takiej samej zasadzie wyświetlane zostają posty znajdujące się pod url powyżej a także ich usuwanie. Dodanie nowego postu:

![](https://i.imgur.com/ll03mp9.png)
 
Po wysłaniu znajduje się on w Completed tasks, ponieważ zaznaczyłam checkbox *finished*.

![](https://i.imgur.com/RkAouz6.png)

Post można edytować, odznaczam *finished*.

![](https://i.imgur.com/nJiXpSs.png)
 
Zadanie *Clean the carpet* znajduje się w Incompleted tasks:

![](https://i.imgur.com/WVMe7Xp.png)

W konsoli:

![](https://i.imgur.com/0AvW5w5.png)

2. ##### Usuwanie posta

Przy kliknięciu delete post znika:
![](https://i.imgur.com/tYKo48q.png)

W konsoli również jest wyświetlone:

![](https://i.imgur.com/KeR0Ld2.png)