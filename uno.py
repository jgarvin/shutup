#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import serial
import time
import signal
import sys
import os

class Uno(object):
    def __init__(self):
        self.reconnect = False
        self.quit = False

    def data_callback(self, data):
        pass

    def user_signal_handler(self, a, b):
        self.reconnect = True

    def interrupt_signal_handler(self, a, b):
        self.quit = True

    def run(self):
        signal.signal(2, self.interrupt_signal_handler)
        signal.signal(16, self.user_signal_handler)
        s = None
        while True:
            print("***Connecting***")
            if s:
                s.close()
                time.sleep(5)
            s = serial.Serial('/dev/ttyACM0', 921600, timeout=1)
            while True:
                try:
                    x = s.readline()
                    self.data_callback(x)
                except serial.serialutil.SerialException as e:
                    print("***Disconnected***")
                    self.reconnect = True
                    if self.quit:
                        sys.exit(1)

                if self.reconnect:
                    self.reconnect = False
                    break

