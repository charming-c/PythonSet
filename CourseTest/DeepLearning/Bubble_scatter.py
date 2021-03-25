import plotly.graph_objs as go
from plotly import offline
'''
x_layout = [10000, 20000, 30000, 40000,
            50000, 60000, 70000, 80000, 90000, 100000]
y_layout = [0.255531, 1.06421, 2.52793,
            4.37861, 6.95507, 10.1844, 14.1177, 18.9485, 22.9223, 28.8163]

trace1 = go.Scatter(
    x=x_layout,
    y=y_layout,
    mode='lines',
    name='冒泡排序',
    marker=dict(color='rgba(16, 112, 2, 0.8)'),
    text=x_layout
)

data = [trace1]
'''
x1_layout = ['10', '100', '1000', '10000', '100000']
y1_layout = [2.6e-05, 8e-05, 0.002611, 0.259262, 28.8163]

trace1 = go.Scatter(
    x=x1_layout,
    y=y1_layout,
    mode='lines',
    name='冒泡排序',
    marker=dict(color='rgba(16, 112, 2, 0.8)'),
    text=x1_layout
)
'''
x2_layout = ['10', '100', '1000', '10000', '100000']
y2_layout = [2.8e-05, 6.8e-05, 0.000504,
             0.005455, 0.056271]

trace2 = go.Scatter(
    x=x2_layout,
    y=y2_layout,
    mode='lines',
    name='希尔排序',
    text=x2_layout
)
'''
x2_layout = [10000, 20000, 30000, 40000,
             50000, 60000, 70000, 80000, 90000, 100000]
y2_layout = [0.005455, 0.012356, 0.016016, 0.024678,
             0.030741, 0.038632, 0.044492, 0.04862, 0.056102, 0.056271]

trace2 = go.Scatter(
    x=x2_layout,
    y=y2_layout,
    mode='lines',
    name='希尔排序',
    marker=dict(color='rgba(16, 112, 2, 0.8)'),
    text=x2_layout
)

x3_layout = [10000, 20000, 30000, 40000,
             50000, 60000, 70000, 80000, 90000, 100000]
y3_layout = [0.001576, 0.003082, 0.005431, 0.006133,
             0.009064, 0.010318, 0.012431, 0.01405, 0.014737, 0.01734]

trace3 = go.Scatter(
    x=x3_layout,
    y=y3_layout,
    mode='lines',
    name='快速排序',
    text=x3_layout
)

data = [trace2, trace3]


layout = dict(title='排序算法折线图',
              # 设置图像的标题
              xaxis=dict(title='排序数据规模', ticklen=5, zeroline=False),
              # 设置x轴名称，x轴刻度线的长度，不显示零线
              yaxis=dict(title='排序所花费的时间(单位/s)', ticklen=5, zeroline=True)
              )

fig = dict(data=data, layout=layout)
offline.plot(fig)
