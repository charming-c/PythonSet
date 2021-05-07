import matplotlib.pyplot as plt
import numpy as np

# Pokémon CP prediction by Linear Model


X_data = [338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
Y_data = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]


# 根据给定的 w,b 求对应的偏导并返回
def Grad(w, b):
    Delt_W = 0.0
    Delt_B = 0.0

    for i in range(0, len(X_data)):
        Delt_W += 2.0*(-X_data[i])*(Y_data[i] - (b + w * X_data[i]))
        Delt_B += (-2.0) * (Y_data[i] - (b+w*X_data[i]))

    return (Delt_W, Delt_B)

# 由于 Model 和 Loss Function 已经确定好了，我们就可以根据对应的模式在functionset里去寻找最好的function


# 初始化一下w,b的值，之后会不停迫近最好的值
w = -100
b = -14
rate = 0.00001

delt_w = 0.0
delt_b = 0.0
(delt_w, delt_b) = Grad(w, b)

w_history = []
b_history = []

while abs(delt_w) > rate or abs(delt_b) > rate:
    print("b: "+str(b)+"\t\t\t w: "+str(w)+"\n"+"b_grad: " +
          str(delt_w)+"\t\t\t w_grad: "+str(delt_b)+"\n")
    w_history.append(w)
    b_history.append(b)
    w -= rate * delt_w
    b -= rate * delt_b
    (delt_w, delt_b) = Grad(w, b)
print("the function will be y_data="+str(b)+"+"+str(w)+"*x_data")

miss = 0.0
for i in range(10):
    miss += abs(Y_data[i]-(b+w*X_data[i]))
average_error = miss/10
print("the average error is "+str(average_error))


fig, ax = plt.subplots()
depth = range(len(w_history))
ax.scatter(w_history, b_history,
           c=depth, cmap=plt.cm.Blues, edgecolor='none', s=8)

ax.set_title('Pokémon')
ax.set_xlabel("w")
ax.set_ylabel("b")
plt.savefig("squares4_plot.png")
