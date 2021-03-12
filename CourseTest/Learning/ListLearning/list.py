players = ['charles','martina','michael','florence','eli']

# 中括号里的负数表示倒数
print(players[-2])

# 冒号表示从哪里到哪里,结尾的下标是终止，不会打印出来,
# 如果冒号前后没有表明值，则前指向列表顶端，后指向列表末尾
print(players[0:4])
print(players[:2])

# 创建切片是可以赋值的
#   people = players
#   这里的people和player是指向同一块存储地址
people = players[0:3]
print(people)
print(people[0])

#for player in players:
#    print(player)

# 不可修改的列表称为元组，区别就是一个用中括号声明，一个用小括号
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 修改元组时的报错
# Traceback (most recent call last):
#   File "/Users/mac/Desktop/python/CourseTest/Learning/ListLearning/list.py", line 26, in <module>
#     dimensions[0] = 100
# TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 100

# 虽然不能修改元组的元素，但可以给存储元组的变量赋值(就是修改指向的元组)，所以一般要修改元组的值，就只能直接定义整个元组
dimensions = (400,100)
print(dimensions)