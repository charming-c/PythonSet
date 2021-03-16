import matplotlib.pyplot as plt
import numpy as np  

x_set = range(1,10001)
y_set = [x**2 for x in x_set]
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.scatter(x_set,y_set,c = y_set,cmap = plt.cm.Blues, s = 8)

ax.set_title('charming')
ax.set_xlabel("value")
ax.set_ylabel("squares")
plt.savefig("squares_plot.png")