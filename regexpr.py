#! /usr/bin/env python

import re

text = []

with open("eingabefile.txt", "w") as f:
    f.writelines("zeile 1 2 3 3 ")
    f.writelines("zeilen 23 23 34 34 ")
    f.writelines("zeilennummer 333 444 555")
   
with open("eingabefile.txt", "r") as f:
    text = f.read()

text2 = re.sub(r"eile", "Paul", text)
text2 = re.sub(r"[3]{3}", "8888", text)

print(text2)





