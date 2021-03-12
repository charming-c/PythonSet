#num = int(input("please enter an integer:"))
#sum = 0
#for i in range(1, num + 1):
#    temp = 1
#    for j in range(1, i + 1):
#        temp *= j
#    sum += temp
#print("the sum is: ",sum)

num = int(input("please enter an integer:"))
sum = 0
temp = 1
if num == 1 or num == 0:
    print("the sum is: 1")
elif num < 0:
    print("invalid!!!")
else:
    for i in range(1, num + 1):
        temp *= i
        sum += temp
    print("the sum is: ",sum)