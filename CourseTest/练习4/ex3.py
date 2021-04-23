with open('歌词.txt','r+') as f:
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    f.write("千千阙歌\n陈慧娴\n")
    for i in range(0,len(lines)):
        f.write(lines[i])
        print(lines[i][:-1])
    f.write('\n由环球唱片发行')
    f.close()