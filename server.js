var express = require('express')
var app = express()
var server = app.listen(8080, function () {
	console.log('HTTP server listening on port 8080')
});
var io = require('socket.io').listen(server)
app.get('/', function (req, res) {
	res.sendFile(__dirname + '/index.html');
});

var udp = require('dgram').createSocket('udp4');
udp.on('listening', function () {
    var address = udp.address();
    console.log('UDP Server listening on ' + address.address + ":" + address.port);
});
udp.on('message', function (message, remote) {
	var msg = JSON.parse(message)
	data[msg.index] = msg.value;
});
udp.bind(7000, "localhost");

var data = new Array(5);
for (var i = 0; i < data.length; i++) {
	data[i] = 0;
}

setInterval(function () { io.emit('update', data); }, 33);

