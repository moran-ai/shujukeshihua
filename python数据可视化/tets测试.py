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

data = pd.read_csv('风景名胜区.csv',encoding='gbk')
# print(data.head())   #  显示前五行数据

# 分组选取湖南的数据
group = data.groupby(by='省份')
data1 =dict([i for i in group])['湖南']
# print(data1)

a = data.loc[data['省份']=='湖南',:]  # 选取湖南的数据
# print(a)

group1 = data1.iloc[:,1:3]
# print(group1)
data2 = data1['总面积(平方公里)']
# print(data2)

# 处理中文乱码
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 折线图
plt.figure(figsize=(10,5))
label = data1['名称'].values
x_num = range(0,len(label))
areal = data1['总面积(平方公里)'].values
plt.plot(x_num,areal,label='总面积',color='r')
plt.title('湖南景点总面积分布图')
plt.ylabel('单位：平方公里')
plt.xticks(x_num,labels=label,rotation=30)
plt.legend(loc='upper right')
# plt.show()

# x = np.arange(data2)
# plt.plot(data2)
# plt.show()
# plt.savefig('湖南景点总面积.jpg')

# 读出湖南省景点游客量数据
plt.figure(figsize=(10,5))
label = data1['名称'].values
x_num1 = range(0,len(label))
areal = data1['总面积(平方公里)'].values
plt.bar(x_num1,areal,label='总面积',color='g')
plt.title('湖南游客分布图')
plt.ylabel('单位：万人次')
plt.xticks(x_num1,labels=label,rotation=30)
plt.legend(loc='upper right')
plt.show()

# 柱状图
data3 = data1['游客量(万人次)']
# plt.figure(figsize=(10,5))
# plt.bar(range(len(data3)),data3)
# plt.show()
# plt.savefig('湖南景点游客量.jpg')

# # 统计全国景点游客量前十的柱状图

df2 = data['游客量(万人次)']
# plt.bar(range(len(df2)),df2)
# plt.show()

# # 统计全国景点游客量前十占比饼图（保留两位小数）
df5 = data.sort_values(by='游客量(万人次)',ascending=False)[:10]
df5.reset_index(inplace=True)  # 重建索引
# x = df5['省份'].values
# x_ticle = (0,len(x))
plt.bar(df5['省份'],df5['游客量(万人次)'],width=0.5)
plt.show()
# print(df2)
# labels = data['名称']
# print(df2)
# plt.figure(figsize=(10,5))
# plt.pie(df2,labels,)
# plt.show()

labels=data['名称'].head(10).values
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
womenCount = data['游客量(万人次)'].head(10)
explode = [0,0,0.1,0,0,0,0, 0, 0, 0] # 确定突出部分
plt.pie(womenCount, explode=explode, labels=labels, shadow=True)
plt.axis('equal')  # 用于显示为一个长宽相等的饼图
plt.show()
