# coding:gbk
import jieba     # 中文分词
from wordcloud import WordCloud  # 词云展示库
import itchat   # 微信库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# with open('停用词表.txt',encoding='utf-8') as  f:
#     stopword = f.read()
#     # print(stopword)
#
# # 读取csv文件
# data = pd.read_csv('商品评价信息.csv',encoding='gbk')
# # print(data)
#
# # 数据处理
# # print(data.drop_duplicates())
# # print(data.dropna(inplace=True))
#
# # 从DataFrame转为字符串
# # 分词
# info = jieba.lcut(str(data['评价信息'].values),cut_all=True)
# # print(info)
#
# # 将得到的info到停用词表去查询，如果不在，则保留
# result=[]
# for word in info:
#     if word in stopword:
#         result.append(word)
# # print(result)
# # 可视化,使用wordcloud
# image = np.array(Image.open('y.jpg'))
# font = r'C:\Windows\Fonts\simkai.ttf'
# w = WordCloud(scale=8,mask=image,font_path=font,background_color='white')
# # w = w.generate(w)
# w = w.generate(''.join(result))     # result(list)->str
# # WordCloud.to_file('1.png')
# plt.imshow(w)
# plt.axis('off')
# plt.show()
data = pd.read_csv('商品评价信息.csv', encoding='gbk')

#  数据处理, 去除重复值
data.drop_duplicates(inplace=True)

# 分词
df = jieba.lcut(str(data['评价信息']), cut_all=True)

# 使用停用词表过滤无用的词

with open('停用词表.txt', encoding='utf-8') as f:  # 读取停用词表
    stopwords = f.read()

# 将得到的 df 到 停用词表去查询，如果不在，有意义的词保留

result = []
for word in df:
    if word not in stopwords:
        result.append(word)

#  可视化， 使用 wordcloud 库

image = np.array(Image.open('y.jpg'))
font = "C:\Windows\Fonts\simkai.ttf"
wc = WordCloud(mask=image, font_path=font, background_color='white')

#   result.(list) -> str
wc = wc.generate(" ".join(result))
plt.imshow(wc)
plt.axis('off')
plt.show()
