#coding:gbk
import pyecharts.options as opts
from pyecharts.faker import  Faker
from pyecharts.charts import Line,Bar
import pandas as pd
df = pd.read_csv('beijing2018AQI.csv',encoding='gbk')
# print(df)
# ����
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
        title_opts=opts.TitleOpts(title='2018����PMȫ������ͼ')
    )

)
line.render('PMȫ��ͼ.html')
