for i in range(1, 10):
    for j in range(i, 10):
        print("{:>2d}*{:d}={}".format(i, j, i*j), end="")
    if(i < j):
        print("\n")
