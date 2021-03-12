target = int(input("please in put a number:"))

print(f"{target} = 1",end = "")

for i in range(2,int(target / 2)):
    while(target % i == 0):
        print(" * ",i,end = "")
        target = target / i

print("\n")