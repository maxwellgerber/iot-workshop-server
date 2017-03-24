var express = require('express')
var app = express()

app.set('port', (process.env.PORT || 5000));

var server = app.listen(app.get('port'), function () {
	console.log('HTTP server listening on port ' + app.get('port'))
});

var io = require('socket.io').listen(server);

app.use(express.static('.'));

var data = new Array(40);

function reset_data(argument) {
	for (var i = 0; i < data.length; i++) {
		data[i] = -1;
	}
}

reset_data();

io.on('connection', function (socket){
	socket.on('data', function (d) {
		console.log(d);
		data[d.i] = d.d;
	})

	socket.on('reset', function (d) {
		console.log("Resetting data now");
		reset_data();
	})
})

setInterval(function () { io.emit('update', data); }, 33);

