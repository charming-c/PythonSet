num = 0
for i in range(1,4+1):
    for j in range(1,4+1):
        for k in range(1,4+1):
            if i==j or i == k or j==k:
                continue
            print(i * 100 + j * 10 + k,end = " ")