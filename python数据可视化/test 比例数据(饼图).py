# coding:gbk
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie

# print(Faker.choose())
# print(Faker.values())
# -> Pie 表示图形的类型
def pie_base() -> Pie:
    c = (
        Pie()
            .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c
pie_base().render('饼图.html')

# Faker.choose() 生成列表
# formatter="{b}: {c}" 格式化数据,b和c位置不可换