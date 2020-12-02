# Lab 4 - REST API z DRF

####
##### Wymagania dotyczące czwartego zadania:
####

![alt text](https://i.imgur.com/TwbYQN0.png)  


---
# Realizacja kodu z zajeć wraz z małymi modyfikacjami

##### Pierwszą stroną jest strona PostList. Na niej widnieją wszystkie posty, a także jest możliwe dodawanie nowych. Jeśli użytkownik jest niezalogowany nie są wyświetlane żadne z istniejących elementów.

1. ### Użytkownik niezalogowany

![alt text](https://i.imgur.com/vQTQPJi.png)  

2. ### Użytkownik zalogowany

![alt text](https://i.imgur.com/ZwZFUfy.png)  

Na stronie możliwe jest również filtrowanie postów.

- Wybranie wyszukiwania postów stworzonych przez użytkownika "Jagoda", rezultat:

![alt text](https://i.imgur.com/mUWp33h.png)  

### Za pomocą routers, możliwe jest pominięcie zapisu,

```
 path('<int:pk>/', PostDetail.as_view()),
```

### dzięki czemu możliwe jest przejście do wybranego posta dopisując jego id po "/". Dzięki czemu dostęp do posszczególnych elementów strony jest znacznie ułatwiony.

Wyświetlenie drugiego posta:

![alt text](https://i.imgur.com/H8kThPR.png)



