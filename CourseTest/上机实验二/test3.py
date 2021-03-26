def isNum(num):
    arr = []
    for i in range(0, 5):
        arr.append(num % 10)
        num = num // 10

    for i in range(0, 2):
        if(arr[i] != arr[4-i]):
            return False
    return True


num = int(input("请输入一个5位整数："))
if(isNum(num)):
    print("是一个回文数")
else:
    print("不是一个回文数")
