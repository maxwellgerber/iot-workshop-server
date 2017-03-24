from socketIO_client import SocketIO
import serial
import argparse

#read in port and station
parser = argparse.ArgumentParser(description='Python utility for HKN IoT Workshop.')
parser.add_argument('--station', help="The station number you are at", type=int, required=True)
parser.add_argument('--port', help="The com port of the MSP you are using", required=True)
args = parser.parse_args()
station = int(args.station)
port = args.port

ser = serial.Serial(port)

with SocketIO('hkn-iot-workshop.herokuapp.com', 80) as sock:
	while True:
		value = ser.readline()
		cleaned = value.decode("utf-8").strip() 
		print("Transmittiong {}".format(cleaned))
		sock.emit('data', {'i':station, 'd':cleaned}) 

