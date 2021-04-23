# count = 1
# with open('text1.txt','r+') as f:
#     lines = f.readlines()
#     f.seek(0)
#     f.truncate()
#     for i in range(0, len(lines)):
#         f.write(str(count) + " ")
#         f.write(lines[i])
#         count += 1
#     f.close()

count = 1
with open('text1.txt','r') as f1:
    lines = f1.readlines()
    with open('text2.txt','w') as f2:
        for i in range(0,len(lines)):
            f2.write(str(count) + '. ')
            f2.write(lines[i])
            count += 1
        f2.close()
        f1.close()