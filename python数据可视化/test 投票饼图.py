# coding:gbk

from pyecharts.charts import Pie
from pyecharts import options as opts
import pandas as pd

data = pd.read_csv('vote_result.csv',encoding='gbk')
# print(data['感兴趣的领域'])

# data['感兴趣的领域'].tolist     ndarray 转list

# radius=["40%", "75%"]添加饼图变为环形图,radius为半径,40%为内半径,75%为外半径
# legend_opts=opts.LegendOpts设置图例

def pie_base():
    c =(
        Pie()
        .add("",[list(z) for z in zip(data['感兴趣的领域'].values.tolist(),
                                      data['票数'].values.tolist())],radius=["40%", "75%"])
            .set_global_opts(title_opts=opts.TitleOpts(title="投票饼图"),
                             legend_opts=opts.LegendOpts(
                             orient="vertical", pos_top="15%", pos_left="2%"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

pie_base().render('投票.html')
