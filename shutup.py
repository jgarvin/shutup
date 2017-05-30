#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os

from uno import Uno

class Shutup(Uno):
    def __init__(self):
        Uno.__init__(self)
        self.muted = None

    def data_callback(self, data):
        if not data:
            return
        
        should_mute = False
        value = int(data)
        should_mute = value < 20
        if self.muted is None or self.muted != should_mute:
            os.system("amixer set Capture {}".format("nocap" if should_mute else "cap"))
            self.muted = should_mute

def main():
    with open("/tmp/.shutup_pid", "w") as f:
        f.write(str(os.getpid()))

    u = Shutup()
    u.run()

if __name__ == "__main__":
    main()