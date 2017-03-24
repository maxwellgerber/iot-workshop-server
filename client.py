from socketIO_client import SocketIO
import serial
import argparse

#read in port and station
parser = argparse.ArgumentParser(description='Process station number and port number.')
parser.add_argument('--station')
parser.add_argument('--port')
args = parser.parse_args()
station = int(args.station)
port = args.port

ser = serial.Serial(port)

with SocketIO('hkn-iot-workshop.herokuapp.com', 80) as sock:
	while True:
		value = ser.readline()
		value = value.decode("utf-8").strip() 
		print(value)
		sock.emit('data', {'i':station, 'd':value}) 
