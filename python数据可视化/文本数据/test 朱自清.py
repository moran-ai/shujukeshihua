# coding:gbk
import jieba     # ���ķִ�
from wordcloud import WordCloud  # ����չʾ��
import itchat   # ΢�ſ�
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
data = pd.read_csv('text.csv', encoding='gbk')

#  ���ݴ���, ȥ���ظ�ֵ
data.drop_duplicates(inplace=True)

# �ִ�
df = jieba.lcut(str(data), cut_all=True)

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
