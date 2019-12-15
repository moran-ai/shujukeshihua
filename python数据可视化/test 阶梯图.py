# coding=gbk
# import pyecharts
# print(pyecharts.__version__)  # 查看版本

from pyecharts.charts import Line   # Line 代表折线图，Bar代表柱状图
import pyecharts.options as opts    # 选项
from  pyecharts.faker import  Faker   # 产生伪数据
# Line()表示构造函数
# is_step=True 变成阶梯图,去掉显示折线图

line9 = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis('data',Faker.values(),is_step=True)
    .set_global_opts(title_opts=opts.TitleOpts(title='Line 阶梯图'))
)
line9.render('阶梯图.html')  # 生成网页文件,括号里不给参数，生成的网页文件是render.html
