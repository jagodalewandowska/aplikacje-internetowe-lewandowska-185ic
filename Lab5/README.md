# Lab 5 - Web Scraping

####
#### Wymagania dotyczące piątego zadania:
####

![alt text](https://i.imgur.com/pUdIE54.png)  

Moja strona podzielona jest parę mniejszych podstron. Oto krótki opis każdej z nich (odnośników w nagłówku):
1. **Strona główn**a - zawiera wymagania do tego ćwiczenia
2. **Przykłady zajęć** - są to wdrożone przykłady zajęć z małymi zmianami
3. **Web Scraping** - czyli utworzony formularz, w którym można wprowadzić adres url oraz element HTML jaki ma być zbadany
4. **XPath oraz xmlx** - wykorzystanie obydwu narzędzi do Web Scrapingu
5. **Github** - odnośnik do mojego Githuba

---
# Wykonanie zadań, zrzuty ekranów stron


## 1. Strona główna

Na stronie głównej zamieściłam wymagania dotyczące zadania.

![alt text](https://i.imgur.com/I9zMjs0.png)


## 2. Przykłady z zajęć - /lab/

Na tej podstronie wyświetlone zostają wdrożone kody z zajęć. Aby możliwe było przekazanie wartości do formularza konieczne było dodanie do każdego ze stworzonych funkcji return i tego, co ma dana funkcja zwracać.

![alt text](https://i.imgur.com/mDD50Do.png)  

### Przykład 1

![alt text](https://i.imgur.com/tf00NnM.png)

Stronę, z której pobieram tag p zamieniłam na [inną](https://starwars.fandom.com/wiki/Star_Wars). Aby móc pobierać taki tag schemat wygląda bardzo podobnie dla każdego z przykładów. Na początek, należy wysłać zapytanie za pomocą polecenia
```
requests.get(' -- nasze url -- ')
```
a następnie przypisać je do jakiejś zmiennej. Następnie przejście do parsowania, gdzie wynik przypisywany jest zwykle jak również w dokumentacji do soup. Trzeba następnie wybrać, gdzie wszystkie szukane elementy będą przechowywane -- do tego dłuży tablica:
```
all_ex = []
```
Na początku jest pusta, ale teraz następuje przejście do wybrania elementów ze strony. Pierwszym z nich jest pierwszy tag p, który jest przypisywany koniecznie do zmiennej. Trzeba sprecyzować, który dokładnie znacznik ma to być w nawiasach kwadratowych, a następnie zamiana na tekst.
```
zmienna = soup.select("tag")[który].text 
```
Tak samo robione jest kolejne:
```
another_p = soup.select("p")[1].text
```
A na koniec zliczana jest ilość znaczników na stronie za pomocą funkcji **len()**. Aby dane można było wyświetlić na stronie należy je wywołać. Aby przekazać je należy dodac na końcu funkcji return(render,...)
```
return render(request,'labs.html',{'first_p':first_p, 'another_p':another_p, 'p_amount':p_amount, ...
```

Ze względu na to, że szukane były pojedyncze wartości do liczenia nie trzeba zastosować pętli. Zmienne muszą być otoczone podwójnymi klamrami {{zmienna}}. Tak wygląda to w kodzie:
```
...
      <b>Pierwszy tag p:</b> {{first_p}} <br>
      <b>Następny tag p:</b> {{another_p}} <br>
      <b>Ilość znaczników p:</b> {{p_amount}}
                                                  ...
```
### Przykład 2

![alt text](https://i.imgur.com/TmfQW12.png)

Następny przykład różni się tym, że wyświetlane będzie wiele wartości ze strony. Początek wygląda tak samo, wysyłane jest zapytnaie, parsowanie oraz tworzenie pustej tablicy. Wybierany jest element, z którego brane będą wartości do wyświetlenia, jest to "div.thumbnail". 

![alt text](https://i.imgur.com/nmoXzzj.png)

Aby znaleźć daną wartość należy zgodnie z kodem przejść do tagu h4, a o wartości title. Brany jest pod uwagę pierwszy napotkany obiekt, co jest zmieniane w pętli. 
```
title = elem.select("h4 > a.title")[0].text
```
Kolejną zmienną będzie ratings, która zapisana jest w klasyczny sposób jak w przykładzie pierwszym. Tworzona jest nowa wartość info, która składa się z obydwu wartości title oraz review, a następnie stosowana jest funkcja strip, likwidujące puste pola będące wynikiem importowania danych.

Po tym do wcześniej utworzonej tablicy dodawane są wszystkie elementy za pomocą funkcji **.append()**. Następnie trzeba dodać na takiej samej zasadzie jak w poprzednim przykładzie w return, render ... 

W formularzu aby dodać wszystkie elementy muszę utworzyć pętlę for:
```
{% for top in top_items %} // ------------ dla wszystkich wartości w tablicy top_items
  <li class="list-group-item list-group-item-info"> 
    <b>Nazwa:</b> {{top.title}}<br> // ---------------- nazwa uzyskana przez przejście do wartości title
    <b>Opinia:</b> {{top.review}}<br> // --------------- opinia uzyskana przez przejście do wartości review
  </li>
{% endfor %}
```

### Przykład 3

![alt text](https://i.imgur.com/xrUe5CZ.png)

Jest to przykład bardzo podobny do poprzednich, jednak dzięki niemu można pozyskać adresy url do obrazów oraz ich wartości alt. Wykonane jest to za pomocą funkcji select() aby wybrać typ 'img', get(), aby otrzymać daną wartość w pętli oraz alt dla nazwy. Dane dodawane są do utworzonej pustej tablicy image_data, a na koniec zwracane dzięki return i render. Wyświetlanie na stronie:
```
{% for im in image_data %}
  <li class="list-group-item list-group-item-info">
    <b>Źródło:</b> {{im.src}}<br>
    <b>Alt:</b> {{im.alt}}<br>
  </li>
{% endfor %} <br>
```

### Przykład 4

![alt text](https://i.imgur.com/rtXmupe.png)

W tym zadaniu wykorzystana jest zmienna wcześniej zadeklarowana products. Dodana jest nowa tablica all_products, w której przechowywane są wszystkie dane: nazwa, opis, cena, opinie, obraz. W kodzie pomieszane są różne metody otrzymywania danych. Przejście do odpowiedniego znacznika a po znaczniku h4 - jak w przykładzie 2, otrzymanie opisu z pierwszego napotkanego znacznika p, przy czym pozbywane jest znowu "whitespaces" za pomocą funkcji strip().

Na koniec renderowanie już wszystkich zmiennych wszystkich zadań:
```
return render(request,'labs.html',{'first_p':first_p, 'another_p':another_p, 'p_amount':p_amount, 'top_items':top_items, 'image_data':image_data, 'all_products':all_products})
```

## Web Scraping, wyszukiwanie - /scraping/ i /scraped/

![alt text](https://i.imgur.com/PtJrqsx.png)  

Na tej stronie możliwe jest podanie dowolnego adresu HTML oraz jakiego elementu szukamy. Dla niego wyświetlone będą wszystkie dane na stronie. Dla przykładu strona z zadaniami [zadaniami](https://zacniewski.gitlab.io/teaching/2020-internet-apps/) szukając elementu **div**.

![alt text](https://i.imgur.com/01jHcMS.png)  

Lista jest dość długa, bo jest to 21 elementów. Pierwsze z nich, gdzie wyświetlane jest ID, nazwa class, tekst, link, src, alt. Aby rozdzielić tekst od tagów typu p, b, itd zamienione one zostały w kodzie na tekst w ten sposób:
```
get_text = i.text
            get_text = get_text.strip() if get_text is not None else "-"
```
![alt text](https://i.imgur.com/1eO7tU0.png)  

Przykład kiedy wyszukiwane są linki na [starym blogu](https://blog-lewandowska.herokuapp.com/):

![alt text](https://i.imgur.com/UyKGsOO.png)  

Wyniki (część) - 6 elementów.

![alt text](https://i.imgur.com/B2PrdJr.png)

Sam kod jest wykorzystaniem przykładów zajęć, jednak na wejściu przypisywane sa wartości dla url oraz elementu. W formularzu **/scraping/** jest to:
```
...
	// konieczna jest nazwa gdzie dane przejdą, a także jaką metodą
    
    <form action="{% url 'scrapped' %}", method="POST" . . . > // <---- scrapped - strona z wynikami

				....
                
      <h5>Input HTML</h5>
      <input type="text" name="web_link" required> // <---- web_link 

				....

      <h5>Input element</h5>
      <input type="text" name="element" required> // <---- element
      
      			....
                
      <button type="submit" class="btn btn-info">Search</button> // <---- submit, aby wysłać
...         
```
Są one przekazywane do funkcji **getHtml**, a parametry przekazane są w ten sposób:
```
website_link = request.POST.get('web_link', None)
element = request.POST.get('element', None)
```
Następne kroki przebiegają tak samo jak w przykładach z zajęć (parsowanie, utworzenie pustej  tablicy, przejście do pętli. Operuje ona na wszystkich elementach na stronie, również przypisując jak wiele jest elementów.

```
url = website_link
source=requests.get(url).text 
all_links = []
soup = BeautifulSoup(source, "html.parser")
```

W pętli natomiast ustalana jest wartość klasy, szukanie id, href (wynikiem jest link), tekst oraz parametry obrazków. Na koniec wszystkie parametry przekazywane są do utworzonej tablicy all_links, która zwracana jest na wyjściu za pomocą polecenia:
```
return render(request, 'scrapped.html', {'all_links':all_links, 'amount': amount, 'url': url, 'element':element})
```
W formularzu **/scrapped/** wyświetlana jest strona która została podana na wejściu wraz z elementem, oraz w pętli dla każdej wartości id, class, link, text, src, alt.

## XPath i xmlx - /xpath/

![alt text](https://i.imgur.com/bZV4WRe.png)

### Przykład 1

Pierwszy przykład polega na wybraniu adresu url, którym jest [ten](https://starwars.fandom.com/wiki/Star_Wars), a następnie za pomocą xpath odnajduję element.

![al text](https://i.imgur.com/VNqXUDH.png)

Znajduję go badając interesujący element na stronie, kopiuję go przez "Copy XPath". Fragment kodu, który odwołuje się do pobranego elementu na liście:
```
path = '//*[@id="toc"]/ul/li[2]/ul/li[1]/ul/li[1]/a'  
```

![alt text](https://i.imgur.com/cRStxEj.png)

Wybierany jest tylko pierwszy element na liście. Po drodze pobierany jest ciąg znaków tak, aby później formstring mógł wykorzystać go do parsowania.

### Przykład 2

Do pobrania z tej samej strony internetowej wykorzystuję fragment kodu, gdzie szukam klasy o nazwie quote.
```
path = '//*[@class="quote"]'   
```

wiedząc, gdzie się znajduje badając element:

![alt text](https://i.imgur.com/VNqXUDH.png)

Wynik:

![alt text](https://i.imgur.com/RH8ZpbY.png)

Jak zawsze aby mieć dostęp do tych wartości trzeba je zrenderować i zwrócić.
```
return render(request, 'xpath.html', {'lxml1': lxml1,'lxml2': lxml2 })
```

W formularzu wyświetlany jest tak jak poprzednie przykłady:
```
Pobrany element:
                        
  <p style="color: rgb(22, 151, 190); font-family:'Pacifico'">
  		{{lxml1}} 
  </p> <br>
```