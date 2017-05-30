#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os

from uno import Uno

class Cat(Uno):
    def data_callback(self, data):
        print(data, end="")

def main():
    with open("/tmp/.smart_cat_pid", "w") as f:
        f.write(str(os.getpid()))

    u = Cat()
    u.run()

if __name__ == "__main__":
    main()