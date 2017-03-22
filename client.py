import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 7000))

def iot(index, value):
    msg = '{"index": '+str(index)+', "value": '+str(value)+'}'
    s.send(str.encode(msg))

def test():
    while True:
        iot(random.randrange(0, 5), random.randrange(0, 256))

