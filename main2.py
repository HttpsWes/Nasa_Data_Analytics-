from collections import *
import matplotlib.pyplot as plt

File= open("NASA_access_log_Jul95")

dates=[]

try:
    for lines in File:
        time=lines.split(' ')[3]
        time=time.split(':')[0]
        time=time.split('[')[1]
        time=time.split('/1995')[0]
        dates.append(time)


except UnicodeDecodeError:
    print('Its ok!')


plt.style.use("dark_background") #Darkground applied to my graph instead of light
time_date= Counter(dates).most_common(10)
dateKeys = Counter(dates).keys()
timevalues = Counter(dates).values()


print(dateKeys) #Data of my Dates
print(timevalues)#Data of my Dates


date_value=[]
date_key=[]

fig, ax = plt.subplots()
for z in time_date:


    date_key.append(z[0])
    date_value.append(z[1])


plt.plot(dateKeys,timevalues, #I added different plot and line colors to my graph to make it more creative
    color='yellow',
    marker="o",
    )

plt.xticks(rotation=30)
ax.grid(color='white') 
plt.xlabel("Month: July ")#Titles of my Graph
plt.ylabel("# of Visits")

plt.show()
print(f"The most frequent date was {Counter(time).most_common(1)}")