x_data = [338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_data = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]
# 计算梯度微分的函数getGrad()


def getGrad(b, w):
    # initial b_grad and w_grad
    b_grad = 0.0
    w_grad = 0.0
    for i in range(10):
        b_grad += (-2.0)*(y_data[i]-(b+w*x_data[i]))
        w_grad += (-2.0*x_data[i])*(y_data[i]-(b+w*x_data[i]))
    return (b_grad, w_grad)


# 这是我自己写的版本，事实证明结果很糟糕。。。
# y_data=b+w*x_data
# 首先，这里没有用到高次项，仅是一个简单的linear model，因此不需要regularization版本的loss function
# 我们只需要随机初始化一个b和w，然后用b_grad和w_grad记录下每一次iteration的微分值；不断循环更新b和w直至两个微分值b_grad和w_grad都为0，此时gradient descent停止，b和w的值就是我们要找的最终参数
b = -120  # initial b
w = -4  # initial w
lr = 0.00001  # learning rate
it = 100000
b_grad = 0.0
w_grad = 0.0
(b_grad, w_grad) = getGrad(b, w)
for i in range(it):
    print("%f\t%f" % (w, b))
    #print("b: "+str(b)+"\t\t\t w: "+str(w)+"\n"+"b_grad: "+str(b_grad)+"\t\t\t w_grad: "+str(w_grad)+"\n")
    b -= lr*b_grad
    w -= lr*w_grad
    (b_grad, w_grad) = getGrad(b, w)
print("the function will be y_data="+str(b)+"+"+str(w)+"*x_data")
error = 0.0
for i in range(10):
    error += abs(y_data[i]-(b+w*x_data[i]))
average_error = error/10
print("the average error is "+str(average_error))
