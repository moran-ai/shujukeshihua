# coding=gbk
# import pyecharts
# print(pyecharts.__version__)  # �鿴�汾

from pyecharts.charts import Line   # Line ��������ͼ��Bar������״ͼ
import pyecharts.options as opts    # ѡ��
from  pyecharts.faker import  Faker   # ����α����
# Line()��ʾ���캯��
# is_step=True ��ɽ���ͼ,ȥ����ʾ����ͼ

line9 = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis('data',Faker.values(),is_step=True)
    .set_global_opts(title_opts=opts.TitleOpts(title='Line ����ͼ'))
)
line9.render('����ͼ.html')  # ������ҳ�ļ�,�����ﲻ�����������ɵ���ҳ�ļ���render.html
