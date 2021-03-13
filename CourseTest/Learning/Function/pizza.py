# 有时候，预先不知道函数要接受多少实参，好在可以使用c中类似指针这样的变量
# 可以自动创建元组

def make_pizza(size,*toppings):
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
#make_pizza(20,'mushroom','green pepper','extra cheese')