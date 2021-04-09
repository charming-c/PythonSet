import random
import numpy

map = {
    0: '红桃',
    1: '方块',
    2: '黑桃',
    3: '梅花'
}
ret = numpy.zeros((4, 13), dtype=int)
count = 0

while(True):
    kind = random.randint(0, 3)
    size = random.randrange(0, 13)
    if(ret[kind][size] == 0):
        if 1 < size <= 9:
            print(f"{map[kind]} {size+1}")
        elif size == 0:
            print(f"{map[kind]} A")
        elif size == 10:
            print(f"{map[kind]} J")
        elif size == 11:
            print(f"{map[kind]} Q")
        else:
            print(f"{map[kind]} K")
        ret[kind][size] = 1
        count += 1
    if(count == 52):
        break
