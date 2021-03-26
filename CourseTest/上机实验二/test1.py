str = input("请输入一行字符:")
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for c in str:
    c = ord(c)
    if(c == 32):
        count1 += 1
        continue
    elif(c >= 48 and c <= 57):
        count2 += 1
    elif((c >= 65 and c <= 90) or (c >= 97) and c <= 122):
        count3 += 1
    else:
        count4 += 1

print(f"字符串中英文字符：{count3}")
print(f"字符串中数字字符：{count2}")
print(f"字符串中空格个数：{count1}")
print(f"其他字符：{count4}")
