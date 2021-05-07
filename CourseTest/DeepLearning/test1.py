import matplotlib.pyplot as plt

x_values = [338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_values = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]

fig, an = plt.subplots()

an.scatter(x_values, y_values, c='green', s=10)

plt.savefig("test1.png")
