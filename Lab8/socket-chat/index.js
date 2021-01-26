const express = require('express');
const app = require('express')();
const path = require('path');
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.use(express.static(path.join(__dirname, '/')));

io.on('connection', (socket) => {
    let addedUser = false;
  
    // Kiedy zostaje utworzona nowa wiadomość
    socket.on('chat message', (data) => {      
      socket.broadcast.emit('chat message', {
        username: socket.username,
        message: data
      });
    });
  
    // Tworzenie nowego użytkownika o danym nicku
    socket.on('add user', (username) => {
      if (addedUser) return;
      // Przypisanie nicku i zmiana statusu
      socket.username = username;
      addedUser = true;
      socket.emit('login');
    });
  
    // Podczas pisania zostanie wyświetlona o tym informacja
    socket.on('typing', () => {
      socket.broadcast.emit('typing', {
        username: socket.username
      });
    });
  
    // Kiedy przestaje pisać dany użytkownik informacja znika
    socket.on('stop typing', () => {
      socket.broadcast.emit('stop typing', {
        username: socket.username
      });
    });
  });

http.listen(3000, () => {
  console.log('listening on *:3000');
});

/* Inicjalizacja aplikacji tak, aby zarządzała funkcją w sposób
dostarczania do serwera http 
Dodanie /, który przenosi na stronę główną 
Zawiera /index.html dzięki czemu cały kod nie będzie istniał tutaj

------------------------------- SOCKET -------------------------------

Podczas połączenia kiedy użytkownik połączy się 
socket.io przekazuje obiekt, nasłuchuje połączenia dla przychodzących 
socket i wypisuje ten fakt w konsoli */

/*
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {

  console.log('New user connected');

  socket.on('disconnect', () => {
    console.log('A User has disconnected');    
  });


  socket.on('messages', (msg) => {
    console.log('message received: ' + msg);
  });

  socket.on('messages', (msg) => {
    io.emit('messages', msg);
  });
});

io.emit('some event', { someProperty: 'some value', otherProperty: 'other value' }); 

http.listen(3000, () => {
  console.log('listening on *:3000');
});

*/