import matplotlib.pyplot as plt
import numpy as np

x_set = [338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_set = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]
# plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.scatter(x_set, y_set, c=y_set, cmap=plt.cm.Blues, s=8)

ax.set_title('charming')
ax.set_xlabel("value")
ax.set_ylabel("squares")
plt.savefig("squares2_plot.png")
