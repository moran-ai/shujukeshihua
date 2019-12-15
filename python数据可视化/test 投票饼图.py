# coding:gbk

from pyecharts.charts import Pie
from pyecharts import options as opts
import pandas as pd

data = pd.read_csv('vote_result.csv',encoding='gbk')
# print(data['����Ȥ������'])

# data['����Ȥ������'].tolist     ndarray תlist

# radius=["40%", "75%"]��ӱ�ͼ��Ϊ����ͼ,radiusΪ�뾶,40%Ϊ�ڰ뾶,75%Ϊ��뾶
# legend_opts=opts.LegendOpts����ͼ��

def pie_base():
    c =(
        Pie()
        .add("",[list(z) for z in zip(data['����Ȥ������'].values.tolist(),
                                      data['Ʊ��'].values.tolist())],radius=["40%", "75%"])
            .set_global_opts(title_opts=opts.TitleOpts(title="ͶƱ��ͼ"),
                             legend_opts=opts.LegendOpts(
                             orient="vertical", pos_top="15%", pos_left="2%"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

pie_base().render('ͶƱ.html')
