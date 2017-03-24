import socket
import random
import serial
import time
import argparse

#read in port and station
parser = argparse.ArgumentParser(description='Process station number and port number.')
parser.add_argument('--station')
parser.add_argument('--port')
args = parser.parse_args()
station = int(args.station)
port = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 7000))
ser = serial.Serial(port)


def iot(index, value):
    msg = '{"index": '+str(index)+', "value": '+str(value).strip()+'}'
    print "sending {}".format(msg)
    s.send(str.encode(msg))

def test():
    while True:
        value = ser.readline()
        print value
        iot(station, value)

test()
