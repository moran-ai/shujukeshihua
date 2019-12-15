# coding:gbk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("���ұ����ⷿ����.csv",encoding='gbk')
print(len(data))
# print(pd.isnull(data).sum())  #ͳ�ƿ�ֵ��Ŀ
# print(data.isnull())  # ����Ƿ��ǿ�ֵ
print(data.drop_duplicates(inplace=True))   #
# print(data.drop_duplicates(subset='������ȥ��')
print(len(data))

# ͳ�Ƽ۸�����
# print(data['�۸�(Ԫ/��)'].sum())

# ����"���(�O)"���е����ݣ�����59.11ƽ����ת��59.11
df = data["���(�O)"].values   # ����ȡ��һ�е�ֵ
# print(df)

# �ַ���תΪ������,ʹ��һ��for���
d = []
for i in df:
    d.append(float(i[:-2]))
print(d)

# �Ż�ԭ����
data["���(�O)"] = d
print(data)

# �����쳣ֵ,,ʹ�ú���replace()�����滻
df1 = data["����"].values
# print(df1.replace('����','��'))
# print(df1.replace('��','��'))

# ����forѭ��
d1 = []
for s in df1:
    d1.append(s.replace('����','��'))
    # d1.append(s.replace('��','��'))
print(d1)
# �Ż�ԭ��������
data['����'] = d1
print(data)

# ͳ��ÿ������ķ�Դ������
"""
1.�½�DataFrame,unique()��ʾȥ���ظ�
2.'��Դ����':[0]*13 ��13�����򣬷��۳�ʼֵΪ0
3.��ʼͳ��,���з���
"""
new_data = pd.DataFrame({'����':data['����'].unique(),'��Դ����':[0]*13})
print(new_data)

# ��ԭ���ݻ����Ͻ��з���,��ͳ����ϸ��Ϣ��
group = data.groupby(by='����').count()
print(group)

# �����ķ�Դ����
new_data['��Դ����'] = group.values
print(new_data)
new_data.sort_values("��Դ����",ascending=False,inplace=True)
print(new_data)
# print(new_data['��Դ����'].sort_values())

# �½�λ��
# ƴ�������С������
data["λ��"] = '������'+data['����'].values+'��'+data["С������"].values
print(data)

# data��new_data��Ϊһ�ű�,�ϲ�������concat(��������ƴ��)concat([ ,])��merge(�����ϲ�)
# df2 = pd.merge(new_data,data)
# print(df2)

# ����
price_df = pd.DataFrame({'����':data['����'].unique(),'�����(�O)':[0]*13})
# �ܼ۸�
sum_price = data['�۸�(Ԫ/��)'].groupby(data['����']).sum()
# print(sum_price)
# ���
price_df['�ܼ۸�']=sum_price.values

# �����
sum_area = data['���(�O)'].groupby(data['����']).sum()

# ���
price_df['�����(�O)']=sum_area.values
print(price_df)
price_df['ƽ�����'] = round(price_df['�ܼ۸�']/price_df['�����(�O)'],2)
print(price_df)

merge_df = pd.merge(new_data,price_df)
print(merge_df)

# ��ֹ����
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

num = merge_df['��Դ����']
price = merge_df['ƽ�����']
# print(num)

# x��̶�
x = [i for i in range(13)]
# print(x)
# ����תΪ�б���to_list
labels = merge_df['����']
print(labels)

# ��ͼ
figure = plt.figure()   #

# ������ͼ
ax1 = figure.add_subplot(111)
# ����ͼ,����ƽ�����
ax1.plot(x,price,'or-',label='�۸�')

# ����ͼ�ϵ���������
for i,(_x,y) in enumerate(zip(x,price)):   # ����enumerate���ڱ���,i��ʾ���к�
    plt.text(_x,y,price[i],color='black')

ax1.set_ylabel(['�۸�'])
ax1.legend(loc='upper left')
# ��������
ax2 = ax1.twinx()  # ����һ��ax1�ľ�������
ax2.bar(x,num,color='green',alpha=0.3,label='����')
ax2.legend(loc='upper right')
ax2.set_ylim([0,2000])
ax2.set_ylabel('����')
plt.xticks(x,labels)  # ���ÿ̶ȵ�����
plt.show()
