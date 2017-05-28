#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import serial
import time
import signal
import sys

reconnect = False
quit = False

def user_signal_handler(a, b):
    global reconnect
    reconnect = True

def interrupt_signal_handler(a, b):
    global quit
    quit = True

def main():
    global reconnect
    global quit
    signal.signal(2, interrupt_signal_handler)
    signal.signal(16, user_signal_handler)
    s = None
    while True:
        print("***Connecting***")
        if s:
            s.close()
            time.sleep(1)
        s = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        while True:
            try:
                x = s.read(100)
                print(x, end="")
            except:
                print("Exception!!!!")
                if quit:
                    sys.exit(1)

            if reconnect:
                reconnect = False
                break

if __name__ == "__main__":
    main()