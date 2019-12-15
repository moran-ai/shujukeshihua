# coding:gbk
import pyecharts.options as opts
from pyecharts.faker import  Faker
from pyecharts.charts import Line,Bar
import numpy as np
import pandas as pd
df = pd.read_csv('beijing2018AQI.csv',encoding='gbk')
data = pd.DataFrame({'Date':df['Date'],'ƽ��AQI':df['AQI']})
# print(data['Date'])
# ƽ����
merage_A = data['ƽ��AQI'].groupby(data['Date']).mean()

attr = ["{}".format(str(i)+'��') for i in range(1,13)]

line = (
    Line()
    .add_xaxis(attr)
    .add_yaxis('�¾�',merage_A)
    .set_global_opts(
        title_opts=opts.TitleOpts(title='2018����AQI�¾�����ͼ')
    )

)
line.render('AQI�¾�ͼ.html')
