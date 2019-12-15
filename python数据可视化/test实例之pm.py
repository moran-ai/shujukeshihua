#coding:gbk
import pyecharts.options as opts
from pyecharts.faker import  Faker
from pyecharts.charts import Line,Bar
import pandas as pd
df = pd.read_csv('beijing2018AQI.csv',encoding='gbk')
# print(df)
# 分类
attr = df['Date'].tolist()
# print(attr)
# v1 = df['AQI'].tolist()
# print(v1)
v2 = df['PM'].tolist()
line = (
    Line()
    .add_xaxis(attr)
    .add_yaxis('data',y_axis=v2)
    .set_global_opts(
        title_opts=opts.TitleOpts(title='2018北京PM全年走势图')
    )

)
line.render('PM全年图.html')
