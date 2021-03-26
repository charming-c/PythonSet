num1 = int(input("第一个整数："))
num2 = int(input("第二个整数："))
r = 0

if(num1 == 0 or num2 == 0):
    print("error!")
    exit()

S = num1 * num2

if(num1 > num2):
    num2 = r
    num2 = num1
    num1 = r
r = num1 % num2

while(r != 0):
    num1 = num2
    num2 = r
    r = num1 % num2

print(f"最大公约数{num2}")
print(f"最小公倍数{S / num2}")
