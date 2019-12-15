# coding:gbk
import json
import os

from pyecharts import options as opts
from pyecharts.charts import Page, Tree

def tree_base() -> Tree:
    data = [
        {
            "children": [
                {"name": "B"},
                {
                    "children": [
                        {"children": [{"name": "I"}], "name": "E"},
                        {"name": "F"},
                    ],
                    "name": "C",
                },
                {
                    "children": [
                        {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
                        {"name": "H"},
                    ],
                    "name": "D",
                },
            ],
            "name": "A",
        }
    ]
    c = (
        Tree()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-����ʾ��"))
    )
    return c
tree_base().render('��.html')

def tree_lr() -> Tree:
    with open(os.path.join( "test.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
        # json.load ���ļ�
        # json.load д���ļ�
        # json.loads ��json�ַ�ת��Ϊpython ����,
        # json.dumps	�� Python �������� JSON �ַ���

    c = (
        Tree()
        .add("", [j], collapse_interval=2)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-���ҷ���"))
    )
    return c

tree_base().render('��ͼ.html')
