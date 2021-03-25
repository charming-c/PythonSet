from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

'''
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

frequencies = {}

for i in range(2, die_1.num_sides * 2+1):
    frequency = results.count(i)
    frequencies[i] = frequency
'''

x1_values = ['冒泡(100)', '冒泡(1000)', '冒泡(10000)']
y1_values = [7.9e-05, 0.002768, 0.24686]

x2_values = ['快排(100)', '快排(1000)', '快排(10000)']
y2_values = [5.5e-05,  0.000501, 0.006209]

x3_values = ['希尔(100)', '希尔(1000)', '希尔(10000)']
y3_values = [1.3e-05,  0.000154, 0.00181]

data = [Bar(x=x1_values, y=y1_values), Bar(
    x=x2_values, y=y2_values), Bar(x=x3_values, y=y3_values)]

x_axis_config = {'title': '排序', 'dtick': 1}
y_axis_config = {'title': '排序的时间'}

my_layout = Layout(title='算法对比', xaxis=x_axis_config,
                   yaxis=y_axis_config, barmode="group")
offline.plot({'data': data, 'layout': my_layout}, filename='d6_html.html')
