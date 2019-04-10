#! /usr/bin/env python

a = 2 + 3j
b = 1 + 2j
c = a + b
print(c)
print(type(c))
print(c.imag)

klingeltext = 'klingeling'
print(klingeltext)


namensliste = []
with open("Namen.txt", "r") as fobj:
    for line in fobj:
        print(line)
        namensliste.append(line.strip())




