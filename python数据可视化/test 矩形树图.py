# coding:gbk
import json
import os
from pyecharts import options as opts
from pyecharts.charts import Page,TreeMap

def treemap_official():
    with open(os.path.join( "test.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
    c = (
        TreeMap()
        .add("��ʾ����", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="������ͼʾ��"))
    )
    return c
treemap_official().render('������ͼ.html')
