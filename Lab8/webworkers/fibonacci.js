self.addEventListener("message", function(e) {
  if(e.data > 0){
    let x = 0, y = 1;
    let arr = [];
    if (e.data === 1 || e.data === 0) {
      postMessage(e.data);
    } else {
      for(let i = 0; i < e.data; i++) {
        arr.push(" " + y);
        y += x;
        x = y - x;
      }
      //console.log(arr);
      postMessage(arr);
    }      
  } else {
    postMessage("Podaj liczbę większą od zera!");
  }
}, false);