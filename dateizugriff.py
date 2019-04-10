#! /usr/bin/env python

import os
import sys

print(os.getcwd())

with open("löschtest.txt", "w") as f:
    f.writelines("line 1")
    f.writelines("line 2")

os.remove("löschtest.txt")

print("Jetzt ist Schluss!")



