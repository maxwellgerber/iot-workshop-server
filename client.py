from socketIO_client import SocketIO

def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

def on_aaa_response(*args):
    print('on_aaa_response', args)

print('shit')
socketIO = SocketIO('hkn-iot-workshop.herokuapp.com', 80)
socketIO.emit('data', {'i':1, 'd': 4}) 
socketIO.emit('data', {'i':2, 'd': 4000}) 
socketIO.emit('data', {'i':3, 'd': 2333}) 
socketIO.emit('data', {'i':4, 'd': 400}) 
socketIO.emit('data', {'i':4, 'd': 33}) 
socketIO.emit('data', {'i':5, 'd': .34}) 
socketIO.emit('data', {'i':6, 'd': .114}) 
socketIO.wait(seconds=5)
print('shit')

# print("shit")
# import serial
# import socket
# import random
# import time

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(('10.142.38.175', 7000))
# ser = serial.Serial("/dev/cu.usbmodem14223")


# def iot(index, value):
#     msg = '{"index": '+str(index)+', "value": '+str(value).strip()+'}'
#     print "sending {}".format(msg)
#     s.send(str.encode(msg))

# def test():
#     while True:
#         value = ser.readline()
#         print value
#         iot(1,value)

# test()