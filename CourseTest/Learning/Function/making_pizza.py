# 代码行import pizza让python打开文件夹pizza.py并将其中所有的代码
# 复制到这个程序中，要调用被导入的模块的函数，可指定被导入模块的名称pizza和函数名make_pizza(),
# 并用句点分隔，这些代码的输出与没有导入模块的原始程序相同

#import pizza

# 导入特定的函数
from pizza import make_pizza as make

make(16,'pepperoin')
make(20,'mushroom','green peppers')