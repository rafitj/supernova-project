// WS Connection
const ws = new WebSocket("ws://127.0.0.1:5015/");

// Recieve Input
ws.onmessage = function(event) {
    data = JSON.parse(event.data);
    console.log(data)
    if (data.game) {
        updateField(data.game);
    }
    if (data.msg) {
        console.log(data.msg)
    }
};

// Send Input
document.onkeydown = function(e) {
    e = e || window.event;
    ws.send(e.key);
};