# coding:gbk
import jieba     # ���ķִ�
from wordcloud import WordCloud  # ����չʾ��
import itchat   # ΢�ſ�
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# with open('ͣ�ôʱ�.txt',encoding='utf-8') as  f:
#     stopword = f.read()
#     # print(stopword)
#
# # ��ȡcsv�ļ�
# data = pd.read_csv('��Ʒ������Ϣ.csv',encoding='gbk')
# # print(data)
#
# # ���ݴ���
# # print(data.drop_duplicates())
# # print(data.dropna(inplace=True))
#
# # ��DataFrameתΪ�ַ���
# # �ִ�
# info = jieba.lcut(str(data['������Ϣ'].values),cut_all=True)
# # print(info)
#
# # ���õ���info��ͣ�ôʱ�ȥ��ѯ��������ڣ�����
# result=[]
# for word in info:
#     if word in stopword:
#         result.append(word)
# # print(result)
# # ���ӻ�,ʹ��wordcloud
# image = np.array(Image.open('y.jpg'))
# font = r'C:\Windows\Fonts\simkai.ttf'
# w = WordCloud(scale=8,mask=image,font_path=font,background_color='white')
# # w = w.generate(w)
# w = w.generate(''.join(result))     # result(list)->str
# # WordCloud.to_file('1.png')
# plt.imshow(w)
# plt.axis('off')
# plt.show()
data = pd.read_csv('��Ʒ������Ϣ.csv', encoding='gbk')

#  ���ݴ���, ȥ���ظ�ֵ
data.drop_duplicates(inplace=True)

# �ִ�
df = jieba.lcut(str(data['������Ϣ']), cut_all=True)

# ʹ��ͣ�ôʱ�������õĴ�

with open('ͣ�ôʱ�.txt', encoding='utf-8') as f:  # ��ȡͣ�ôʱ�
    stopwords = f.read()

# ���õ��� df �� ͣ�ôʱ�ȥ��ѯ��������ڣ�������Ĵʱ���

result = []
for word in df:
    if word not in stopwords:
        result.append(word)

#  ���ӻ��� ʹ�� wordcloud ��

image = np.array(Image.open('y.jpg'))
font = "C:\Windows\Fonts\simkai.ttf"
wc = WordCloud(mask=image, font_path=font, background_color='white')

#   result.(list) -> str
wc = wc.generate(" ".join(result))
plt.imshow(wc)
plt.axis('off')
plt.show()
