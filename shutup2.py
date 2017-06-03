#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys
import time
import math

from uno import Uno

class Entry(object):
    def __init__(self, receive_time, reading):
        self.receive_time = receive_time
        self.reading = reading

class MovingAverage(object):
    def __init__(self, interval):
        self.total = 0
        self.interval = interval
        self.history = []

    def update(self, receive_time, reading):
        self.history.append(Entry(receive_time, reading))
        self.total += reading

        remove_count = 0
        for entry in self.history:
            if receive_time - entry.receive_time > self.interval:
                remove_count += 1
                self.total -= entry.reading
            else:
                break

        self.history = self.history[remove_count:]

        return self.value

    @property
    def value(self):
        return self.total / len(self.history)

class Shutup(Uno):
    def __init__(self):
        Uno.__init__(self)
        self.muted = None
        self.average = MovingAverage(25.0/1000.0) # 25ms

    def data_callback(self, data):
        if not data:
            return

        try:
            reading = int(data)
            reading = math.log(float(reading)) if reading else 0
        except ValueError:
            print("Ignoring bad data: {}".format(data), file=sys.stderr)
            return

        receive_time = time.time()
        self.average.update(receive_time, reading)

        # print(self.daverage.value)
        # print(self.average.value)

        value = self.average.value

        should_mute = value < 1
        if self.muted is None or self.muted != should_mute:
            print(value)
            os.system("amixer set Capture {}".format("nocap" if should_mute else "cap"))
            self.muted = should_mute

def main():
    with open("/tmp/.shutup_pid", "w") as f:
        f.write(str(os.getpid()))

    u = Shutup()
    u.run()

if __name__ == "__main__":
    main()