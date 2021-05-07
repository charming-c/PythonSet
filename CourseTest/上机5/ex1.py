from os import path
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import jieba
# jieba.enable_parallel(4)


with open("data.txt", encoding='utf-8') as f:
    data = f.read()
    f.close()

seg_list = jieba.lcut(data,  cut_all=False)
res = {}
for item in seg_list:
    if item in res.keys():
        res[item] += 1
    else:
        res[item] = 1


wordcloud = WordCloud(
    background_color='white',  # 设置背景颜色  默认是black
    width=900, height=600,
    max_words=100,            # 词云显示的最大词语数量
    max_font_size=99,         # 设置字体最大值
    min_font_size=16,         # 设置子图最小值
    random_state=50,           # 设置随机生成状态，即多少种配色方案
    font_path="SourceHanSerifK-Light.otf").generate_from_frequencies(res)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
