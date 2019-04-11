#! /usr/bin/env python

import json
import matplotlib.pyplot as plt

personendaten = [["Peter", "1974", "1,78m"], ["Paula", "1987", "1,68m"], ["Petra", "1976", "1,73m"]]

with open("JsonFile", "w") as fobj:
    json.dump(personendaten, fobj)

# Generate large JSON file
hoehendaten = []

for i in range(1000):
    if(i < 300):
        hoehendaten.append([i, "300"])
    else:
        hoehendaten.append([i, "500"])
        

with open("JSONFunktionswerte", "w") as fobj:
    json.dump(hoehendaten, fobj)

plt(hoehendaten)
plt.grid(True)
plt.show()




