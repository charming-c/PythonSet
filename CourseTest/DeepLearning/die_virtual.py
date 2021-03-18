from die import Die 
from plotly.graph_objs import Bar,Layout
from plotly import offline

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

frequencies = {}

for i in range(2,die_1.num_sides * 2+1):
    frequency = results.count(i)
    frequencies[i] = frequency


x_values = list(range(2,die_1.num_sides * 2+1))
y_values = list(frequencies.values())
data = [Bar(x = x_values, y = y_values)]

x_axis_config = {'title':'结果','dtick' : 1}
y_axis_config = {'title':'结果的频率'}

my_layout = Layout(title = '掷两个D6 1000次结果', xaxis = x_axis_config,
                     yaxis = y_axis_config)
offline.plot({'data':data,'layout' : my_layout}, filename = 'd6_html')