import matplotlib.pyplot as plt
import numpy as np 
from collections import *

log = open("NASA_access_log_Jul95")

from collections import Counter

ip_address = []
time = []
data = []


try:
    for line in log:
        
        ip_address.append(line.split(" ")[0])

except:
    print("its correct")

print(ip_address)

c = Counter(ip_address)

newDict = dict()

for key,value in c.items():
    if value >= 150:
        newDict[key] = value



print(newDict.keys())
print(newDict.values())
plt.bar (newDict.keys(), newDict.values())
plt.show()


#plt.show()





#print(f"the most common ip address is:" , c)

