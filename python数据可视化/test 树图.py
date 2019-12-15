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
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    )
    return c
tree_base().render('树.html')

def tree_lr() -> Tree:
    with open(os.path.join( "test.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
        # json.load 读文件
        # json.load 写入文件
        # json.loads 将json字符转换为python 对象,
        # json.dumps	将 Python 对象编码成 JSON 字符串

    c = (
        Tree()
        .add("", [j], collapse_interval=2)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-左右方向"))
    )
    return c

tree_base().render('树图.html')
