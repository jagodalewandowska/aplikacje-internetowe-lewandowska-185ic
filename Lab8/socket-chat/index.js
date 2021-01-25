/* Inicjalizacja aplikacji tak, aby zarządzała funkcją w sposób
dostarczania do serwera http */
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

/* Dodanie /, który przenosi na stronę główną 
Zawiera /index.html dzięki czemu cały kod nie będzie istniał tutaj */
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

/* ------------------------------- SOCKET ------------------------------- */

/* Podczas połączenia kiedy użytkownik połączy się 
socket.io przekazuje obiekt, nasłuchuje połączenia dla przychodzących 
socket i wypisuje ten fakt w konsoli */
io.on('connection', (socket) => {
  console.log('a user connected');
});

/* Dołączanie użytkowników */
io.on('connection', (socket) => {
  console.log('a user connected');
  socket.on('disconnect', () => {
    console.log('user disconnected');
  });
});

/* Wyświetlanie wiadomości na w konsoli */
io.on('connection', (socket) => {
  socket.on('mymessage', (msg) => {
    console.log('message received: ' + msg);
  });
});

/* Aby móc wysyłać wiadomości do wszystkich podłączonych "gniazd"
wykorzystywana jest metoda io.emit() */
io.emit('some event', { someProperty: 'some value', otherProperty: 'other value' }); 

/* Wysyłanie wiadomości do wszystkich, łącznie z wysyłającym */
io.on('connection', (socket) => {
  socket.on('mymessage', (msg) => {
    io.emit('mymessage', msg);
  });
});

/* Nasłuchiwanie portu 3000 - na którym będzie serwer */
http.listen(3000, () => {
  console.log('listening on *:3000');
});