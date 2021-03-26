def move(n, A, B, C):

  # 递归函数现调用出口
    if n == 1:
        C.append(A[-1])
        A.pop()
        return
    else:
        move(n-1, A, C, B)  # 借助C将A中n-1个的移动到B上，这也是我们定义move函数的意义
        C.append(A[-1])  # 将A的最下面的移动到c上，一次move的目的完成
        A.pop()  # 将A中的第一个弹出去，此时A是空的，在下一次递归时我们的B应该是这一次的A
        move(n-1, B, A, C)


def hanota(A, B, C):
    n = len(A)
    move(n, A, B, C)
    print(A)
    print(B)
    print(C)


A = [1, 2, 3, 4, 5]
B = []
C = []

hanota(A, B, C)
