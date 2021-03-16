from die import Die 
from plotly.graph_objs import Bar,Layout
from plotly import offline

die = Die()

results = []
for roll_num in range(1000):
    results.append(die.roll())

frequencies = {}

for i in range(1,die.num_sides+1):
    frequency = results.count(i)
    frequencies[i] = frequency


x_values = list(range(1,die.num_sides+1))
y_values = list(frequencies.values())
data = [Bar(x = x_values, y = y_values)]

x_axis_config = {'title':'结果'}
y_axis_config = {'title':'结果的频率'}

my_layout = Layout(title = '掷一个D6 1000次结果', xaxis = x_axis_config,
                     yaxis = y_axis_config)
offline.plot({'data':data,'layout' : my_layout}, filename = 'd6_html')