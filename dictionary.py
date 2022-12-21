import matplotlib.pyplot as plt
import numpy as np 
from collections import *

fruits = [

    'apple',
    'banana','banana',
    'grapes','grapes','grapes',
    'orange','orange','orange','orange', 

]

fruits_counter = Counter(fruits)

print(fruits_counter)

print(fruits_counter.keys())
print(fruits_counter.values())

plt.bar (fruits_counter.keys(), fruits_counter.values())

plt.show()

