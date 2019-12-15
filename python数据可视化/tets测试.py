# coding=gbk
# ser_obj=pd.Series(np.arange(1,6),index=[5,3,0,4,2])
#
# print(ser_obj.sort_index())

# # print((pd.DataFrame([[2,3],]*3,columns=['A','B'])).apply(lambda x:x+1))
# df1 = pd.DataFrame(data=np.random.randint,index=['B','D','A','C'],
#                    columns=['d','b', 'c','a'])
# print(df1)

# np.random.seed(42)
# df1=pd.DataFrame(np.random.randint(1,10,(4,4)),index=['B','D','A','C'],
#                  columns=['d','b','c','a'])
# print(df1)

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('�羰��ʤ��.csv',encoding='gbk')
# print(data.head())   #  ��ʾǰ��������

# ����ѡȡ���ϵ�����
group = data.groupby(by='ʡ��')
data1 =dict([i for i in group])['����']
# print(data1)

a = data.loc[data['ʡ��']=='����',:]  # ѡȡ���ϵ�����
# print(a)

group1 = data1.iloc[:,1:3]
# print(group1)
data2 = data1['�����(ƽ������)']
# print(data2)

# ������������
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# ����ͼ
plt.figure(figsize=(10,5))
label = data1['����'].values
x_num = range(0,len(label))
areal = data1['�����(ƽ������)'].values
plt.plot(x_num,areal,label='�����',color='r')
plt.title('���Ͼ���������ֲ�ͼ')
plt.ylabel('��λ��ƽ������')
plt.xticks(x_num,labels=label,rotation=30)
plt.legend(loc='upper right')
# plt.show()

# x = np.arange(data2)
# plt.plot(data2)
# plt.show()
# plt.savefig('���Ͼ��������.jpg')

# ��������ʡ�����ο�������
plt.figure(figsize=(10,5))
label = data1['����'].values
x_num1 = range(0,len(label))
areal = data1['�����(ƽ������)'].values
plt.bar(x_num1,areal,label='�����',color='g')
plt.title('�����οͷֲ�ͼ')
plt.ylabel('��λ�����˴�')
plt.xticks(x_num1,labels=label,rotation=30)
plt.legend(loc='upper right')
plt.show()

# ��״ͼ
data3 = data1['�ο���(���˴�)']
# plt.figure(figsize=(10,5))
# plt.bar(range(len(data3)),data3)
# plt.show()
# plt.savefig('���Ͼ����ο���.jpg')

# # ͳ��ȫ�������ο���ǰʮ����״ͼ

df2 = data['�ο���(���˴�)']
# plt.bar(range(len(df2)),df2)
# plt.show()

# # ͳ��ȫ�������ο���ǰʮռ�ȱ�ͼ��������λС����
df5 = data.sort_values(by='�ο���(���˴�)',ascending=False)[:10]
df5.reset_index(inplace=True)  # �ؽ�����
# x = df5['ʡ��'].values
# x_ticle = (0,len(x))
plt.bar(df5['ʡ��'],df5['�ο���(���˴�)'],width=0.5)
plt.show()
# print(df2)
# labels = data['����']
# print(df2)
# plt.figure(figsize=(10,5))
# plt.pie(df2,labels,)
# plt.show()

labels=data['����'].head(10).values
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
womenCount = data['�ο���(���˴�)'].head(10)
explode = [0,0,0.1,0,0,0,0, 0, 0, 0] # ȷ��ͻ������
plt.pie(womenCount, explode=explode, labels=labels, shadow=True)
plt.axis('equal')  # ������ʾΪһ��������ȵı�ͼ
plt.show()
