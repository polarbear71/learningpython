#! /usr/bin/env python

import numpy
import numpy as np
import matplotlib.pyplot as plt

my_string = 'teststring'
my_string = my_string * 2

print(my_string)

my_string = my_string + ' noch ein Text'
print(my_string)

my_list = [1, 2, 4, 2]
my_array = np.array(my_list)

print(my_array)
print(my_array[:3])

my_list2 = [1, 3, 4, 5]
my_array2 = np.array(my_list2)

plt.plot(my_list, my_list2, color='red', marker='o', linestyle='solid', linewidth='3', markersize='20')
plt.show()





