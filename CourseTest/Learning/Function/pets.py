'''python 是有形参实参之分的'''

'''def increase(a):
       a+=1
       print(a)

   b = 2
   increase(b)
   print(b)'''

def describe_pet(animal_type,pet_name):
    '''显示宠物信息'''
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}")

describe_pet("dog","wangcai")

# 关键字实参，可以忽略传递参数的顺序
describe_pet(animal_type='dog',pet_name='wangcai')
describe_pet(pet_name="wangcai",animal_type="dog")