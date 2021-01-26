$(function() {
    const $window = $(window);
    const $usernameInput = $('.usernameInput'); 
    const $messages = $('.messages');           
    const $inputMessage = $('.inputMessage');  
    const $loginPage = $('.login.page');        
    const $chatPage = $('.chat.page');     
    const socket = io();

    // Lista dostępnych kolorów
    const COLORS = [
        '#6699ff', '#8080ff', '#7070db', '#8c8cd9',
        '#bf80ff', '#3399ff', '#0099cc', '#6495ED'
    ];

    let username;
    let connected = false;
    let typing = false;    
  
    // Ustawienie nazwy użytkownika
    const setUsername = () => {
      username = $usernameInput.val().trim();
      console.log(username)
      if (username) {
        $loginPage.hide();
        $chatPage.show();
        $currentInput = $inputMessage.focus();         
        socket.emit('add user', username);
      }
    }

    // Pobieranie koloru użytkownika
    const getUsernameColor = (username) => {
      // Wyliczenie kodu hash
      let hash = 7;
      for (let i = 0; i < username.length; i++) {
        hash = username.charCodeAt(i) + (hash << 5) - hash;
      }
      // Obliczenie koloru z danym indeksem
      const index = Math.abs(hash % COLORS.length);
      return COLORS[index];
    }
    
    // Wyślij wiadomość
    const sendMessage = () => {
      let message = $inputMessage.val().trim();
      // Jeśli otrzymana zostanie wiadomość a użytkownik będzie połączony
      if (message && connected) {        
        $inputMessage.val('');
        // wywołanie funkcji dodawania wiadomości na czat
        addChatMessage({ username, message });
        // przesył wiadomości za pomocą funkcji chat message na serwer
        socket.emit('chat message', message);
      }
    }
  
    // Dodawanie wiadomości w czacie
    const addChatMessage = (data, options) => {
      if (!options) {
        options = {};
      }
      const $usernameDiv = $('<span class="username"/>')
        .text(data.username)
        .css('color', getUsernameColor(data.username))
      const $messageBodyDiv = $('<span class="messageBody">')
        .text(data.message);
  
      const typingClass = data.typing ? 'typing' : '';
      const $messageDiv = $('<li class="message"/>')
        .data('username', data.username)
        .addClass(typingClass)
        .append($usernameDiv, $messageBodyDiv);
  
      addMessageElement($messageDiv, options);
    }
  
    // Dodaje wiadomości poniżej, po czym wykonuje scroll w dół
    // el - to element, który dodawany jest jako wiadomość
    const addMessageElement = (el, options) => {
      const $el = $(el);
      if (!options) {
        options = {};
      }
      if (typeof options.prepend === 'undefined') {
        options.prepend = false;
      }
      if (options.prepend) {
        $messages.prepend($el);
      } else {
        $messages.append($el);
      }
        // scroll
      $messages[0].scrollTop = $messages[0].scrollHeight;
    }

    // Wyświetlanie napisu "is typing"
    const addChatTyping = (data) => {
      data.typing = true;
      data.message = 'is typing...';
      addChatMessage(data);
    }
  
    // Usuwanie wyświetlenia "is typing"
    const removeChatTyping = (data) => {
      getTypingMessages(data).fadeOut(function () {
        $(this).remove();
      });
    }    
  
    // Aktualizacja napisu "typing"
    const updateTyping = () => {
      if (connected) {
        if (!typing) {
          typing = true;
          socket.emit('typing');
        }
      }
    }
  
    // Zwracanie nazwy użytkownika, który pisze w tym momencie
    const getTypingMessages = (data) => {
      return $('.typing.message').filter(function (i) {
        return $(this).data('username') === data.username;
      });
    }
  
    // Wykrywanie przycisku enter
    $window.keydown(event => {
        // enter to 13
      if (event.which === 13) {          
        if (username) {
          sendMessage();
          socket.emit('stop typing');
          typing = false;
        } else {
        // ustawienie użytkownika jeśli nie jest zapisany
          setUsername();
        }
      }
    });

    // Wywołanie funkcji updateTyping wyświetlającej "typing"
    $inputMessage.on('input', () => {
      updateTyping();
    });  
  
    // Pozostałe wywołania -- login, chat message, pisanie, koniec pisania
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
  });