import matplotlib.pyplot as plt
import numpy as np

#Chart #1

#values for me graph
x = list(range(0,10))
y = list(range(-10,0))

#plot command that plots data
plt.plot(x,y)

#plot command that displays my data
plt.show()

#Chart #2

#values of the height/weight of track team members
a = [5,7,8,7,2,17,2,9,4,11,12,9,6]
b = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#plot command that gives a title for a graph or chart
plt.title("Track Team height")

#plot command for x/y labels
plt.xlabel("height")
plt.ylabel("weight")

#plot command that scatters my data (specificliy for scatter plots)
plt.scatter(a, b)

#plot command that displays my data
plt.show()

#Chart #3

#Values for me pie chart
y = np.array([35, 25, 25, 15])
plt.title("Brooklyn Steam Pathways")

pathways = ["CS/IT", "D&E", "F&M", "Construction"]

#Spacing used for the data in my pie chart
myexplode = [0.2, 0, 0, 0]

#command that allows me to plot my data and i added some values to make it more asestheticly pleasing.
plt.pie(y, labels = pathways, explode = myexplode, shadow = True)

#plot command that displays my data
plt.show() 



ip_common = Counter(ip_address).most_common(10)
ip_values=[]
ip_keys=[]


for i in ip_common:
    ip_keys.append(i[0])
    ip_values.append(i[1])

plt.bar(ip_keys,ip_values)

plt.show()


#time_common= Counter(time).most_common(10)
#time_value=[]
#time_key=[]


#For a in time_common:
   # time_key.append(a[0])
   # time_value.append(a[1])

#plt.plot(time_key,time_value)
#plt.xticks(rotation=90)

print(c.keys())
print(c.values())
plt.bar (c.keys(), c.values())
plt.show()
