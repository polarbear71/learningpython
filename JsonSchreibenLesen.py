#! /usr/bin/env python

import json

personendaten = [["Peter", "1974", "1,78m"], ["Paula", "1987", "1,68m"], ["Petra", "1976", "1,73m"]]

with open("JsonFile", "w") as fobj:
    json.dump(personendaten, fobj)

