list = []
for i in range(1, 21):
    if(i == 1 or i == 2):
        print("{:>5d}".format(1), end="")
        list.append(1)
    else:
        list.append(list[-1] + list[-2])
        print("{:>5d}".format(list[-1] + list[-2]), end="")
    if(i % 4 == 0):
        print('\n')
