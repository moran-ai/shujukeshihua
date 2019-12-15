# coding:gbk
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie

# print(Faker.choose())
# print(Faker.values())
# -> Pie ��ʾͼ�ε�����
def pie_base() -> Pie:
    c = (
        Pie()
            .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-����ʾ��"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c
pie_base().render('��ͼ.html')

# Faker.choose() �����б�
# formatter="{b}: {c}" ��ʽ������,b��cλ�ò��ɻ�