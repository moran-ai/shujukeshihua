# coding=gbk
from pyecharts.charts import Bar   # Bar代表柱状图


bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()

from pyecharts.charts import Bar
from pyecharts import options as opts
bar = Bar()  # 构造方法
bar.add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"]) # 添加x轴数据
bar.add_yaxis("商家A裤子销量", [200, 300, 280,230, 360, 210] )  # 添加y轴数据
# 设置全局变量
bar.set_global_opts(title_opts=opts.TitleOpts(title="月份的商品销售图", subtitle="副标题"))
bar.render("mycharts.html")  # 生成本地网页文件

