# coding=gbk
from pyecharts.charts import Bar   # Bar������״ͼ


bar = Bar()
bar.add_xaxis(["����", "��ë��", "ѩ����", "����", "�߸�Ь", "����"])
bar.add_yaxis("�̼�A", [5, 20, 36, 10, 75, 90])
# render �����ɱ��� HTML �ļ���Ĭ�ϻ��ڵ�ǰĿ¼���� render.html �ļ�
# Ҳ���Դ���·���������� bar.render("mycharts.html")
bar.render()

from pyecharts.charts import Bar
from pyecharts import options as opts
bar = Bar()  # ���췽��
bar.add_xaxis(["1��", "2��", "3��", "4��", "5��", "6��"]) # ���x������
bar.add_yaxis("�̼�A��������", [200, 300, 280,230, 360, 210] )  # ���y������
# ����ȫ�ֱ���
bar.set_global_opts(title_opts=opts.TitleOpts(title="�·ݵ���Ʒ����ͼ", subtitle="������"))
bar.render("mycharts.html")  # ���ɱ�����ҳ�ļ�

