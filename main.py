log = open("NASA_access_log_Jul95")

from collections import Counter

ip_address = []


try:
    for line in log:
        
        ip_address.append(line.split(" ")[0])

except:
    print("its correct")

print(ip_address)

c = Counter(ip_address).most_common(3)

print(c)
