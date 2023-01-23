import matplotlib.pyplot as plt
import numpy as np 
from collections import *

log = open("NASA_access_log_Jul95")

from collections import Counter


ip_address = []



try:
    for line in log:
        
        ip_address.append(line.split(" ")[0])

except:
    print("its correct")


print(ip_address)

c = Counter(ip_address) #Counter is used to counter track the amount of ip addresses i set.

newDict = dict()

for key,value in c.items():
    if value >= 900: #Value of Ip addresses that will display on my graph
        newDict[key] = value



print(newDict.keys()) #Data of my ip address
print(newDict.values()) #Data of my ip address



plt.bar(newDict.keys(),newDict.values(), color=['Orange', 'Black',],) #Changed
plt.xticks(rotation= 30 )
plt.rcParams['font.size'] = 5
plt.ylabel("# Of Times Visited", size=15) #Titles of my graphes
plt.title("IP Adresses ", size= 18)

plt.show()

print(f"the most common ip address is {Counter(ip_address).most_common(1)}")

print()

