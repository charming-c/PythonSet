#导入模块，并指定别名plt
import matplotlib.pyplot as plt
import pylab
pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']

input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]

# 这里提示使用何种风格
plt.style.use('seaborn-bright')

# 在这里生成表格，fig表示的是整张图片，ax则指代这里的一个或者多个表格
fig, ax = plt.subplots()
#ax.plot(squares)

# 这里的plot（）函数根据给定的数据进行一个绘制有意义的图表
ax.plot(input_value,squares, linewidth = 2)

#设置图表标题并给坐标轴加上标签
ax.set_title("value",fontsize = 20)
ax.set_xlabel("value-x", fontsize = 14)
ax.set_ylabel("square_y", fontsize = 14)

# 设置刻度标记的大小
ax.tick_params(axis = 'both', labelsize = 10)

#styles = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 
#            'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 
#            'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 
#            'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 
#            'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 
#            'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 
#            'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

plt.show()
