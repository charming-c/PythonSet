user_0 = {
    'username' : 'dfermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

# 这里的遍历方式有点特殊，要用相应的items()方法
# 这个items()方法会返回一个键值对列表
for key,value in user_0.items():
    print('key:',key)
    print('value:',value)

# 遍历字典中的全部的键
for key in user_0.keys():
    print(f"key:{key}")

# 甚至可以使用这个方法来查询某个键是否存在
if 'lala' not in user_0.keys():
    print(f"lala is not in the dictionary")

# 按特定顺序遍历字典的键/值
for name in sorted(user_0.keys()):
    print(f"sorted key:{name}")

for value in sorted(user_0.values()):
    print(f"sorted value:{value}")

# 通过对包含重复元素的列表调用set()，可以让python找出列表独一无二的元素，并使用这些元素创建一个集合
# 集合也可以使用花括号定义，但里面没有顺序和重复元素

num = {'1','2','3','7','5','2','2'}
print(num)