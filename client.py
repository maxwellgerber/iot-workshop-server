import socket
import random
import serial
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 7000))
ser = serial.Serial("/dev/cu.usbmodem14223")


def iot(index, value):
    msg = '{"index": '+str(index)+', "value": '+str(value).strip()+'}'
    print "sending {}".format(msg)
    s.send(str.encode(msg))

def test():
    while True:
        value = ser.readline()
        print value
        iot(1,value)

test()