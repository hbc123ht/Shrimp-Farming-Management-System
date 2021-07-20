$(document).ready(function () {
//    let socket = new WebSocket(`ws://127.0.0.1:8000/?session_key=${sessionKey}`);
    var socket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/' + CurrentUser + '/');
  
    socket.onmessage = function (e) {
        console.log(e.data);
        document.getElementById('name').innerHTML = 123;

    };
});