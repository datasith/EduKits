import numpy as np
import matplotlib.pyplot as plt 
import datetime as DT

data= np.loadtxt('daily_count.csv', delimiter=',', dtype={'names': ('date', 'count'),'formats': ('S10', 'i4')} )

x = []
y = []

for (key, value) in data:
    x.append(DT.datetime.strptime(key,"%Y-%m-%d"))
    y.append(value)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid()

fig.autofmt_xdate()

plt.plot(x,y,'b--o--')
plt.xlabel('Date')
plt.ylabel('Daily Count')
plt.title('Daily Count since February')

plt.savefig("dataviz.png")
