__author__ = 'ATUL'
'''
This is a file for controlling keyboard events.
'''
from pykeyboard import PyKeyboard
import serial
import time
 
comPort = raw_input("Please enter the COM port number")
baudRate = raw_input("Please enter the baud rate")
myserial = serial.Serial(comPort, baudRate)
k = PyKeyboard()
TRUE = 1;
try:
    while (TRUE):
        if (myserial.inWaiting()):
            mydata = myserial.readline()
            x = int(mydata)
            print(x)
            if x == 3:
                k.tap_key(k.left_key)
                print("left")
                time.sleep(1)
            if x == 4:
                k.tap_key(k.right_key)
                print("right")
                time.sleep(1)
            if x == 1:
                k.tap_key(k.up_key)
                print("up")
                time.sleep(1)
            if x == 2:
                k.tap_key(k.down_key)
                print("down")
                time.sleep(1)
except KeyboardInterrupt:
    print("stop")
