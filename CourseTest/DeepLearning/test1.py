import matplotlib.pyplot as plt

x_values = range(1,501)
y_values = [y**3 for y in x_values]

fig, an = plt.subplots()

an.scatter(x_values,y_values,c = 'green', s = 10)

plt.savefig("test1.png")