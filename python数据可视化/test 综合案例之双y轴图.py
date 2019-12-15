# coding:gbk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("链家北京租房数据.csv",encoding='gbk')
print(len(data))
# print(pd.isnull(data).sum())  #统计空值数目
# print(data.isnull())  # 检测是否是空值
print(data.drop_duplicates(inplace=True))   #
# print(data.drop_duplicates(subset='对子列去重')
print(len(data))

# 统计价格总数
# print(data['价格(元/月)'].sum())

# 处理"面积(㎡)"这列的数据，例如59.11平方米转成59.11
df = data["面积(㎡)"].values   # 首先取出一列的值
# print(df)

# 字符串转为浮点数,使用一个for语句
d = []
for i in df:
    d.append(float(i[:-2]))
print(d)

# 放回原数据
data["面积(㎡)"] = d
print(data)

# 处理异常值,,使用函数replace()进行替换
df1 = data["户型"].values
# print(df1.replace('房间','室'))
# print(df1.replace('卫','厅'))

# 利用for循环
d1 = []
for s in df1:
    d1.append(s.replace('房间','室'))
    # d1.append(s.replace('卫','厅'))
print(d1)
# 放回原来的数据
data['户型'] = d1
print(data)

# 统计每个区域的房源总数量
"""
1.新建DataFrame,unique()表示去除重复
2.'房源数量':[0]*13 有13个区域，房价初始值为0
3.开始统计,进行分组
"""
new_data = pd.DataFrame({'区域':data['区域'].unique(),'房源数量':[0]*13})
print(new_data)

# 在原数据基础上进行分组,并统计详细信息、
group = data.groupby(by='区域').count()
print(group)

# 分组后的房源数量
new_data['房源数量'] = group.values
print(new_data)
new_data.sort_values("房源数量",ascending=False,inplace=True)
print(new_data)
# print(new_data['房源数量'].sort_values())

# 新建位置
# 拼接区域和小区名称
data["位置"] = '北京市'+data['区域'].values+'区'+data["小区名称"].values
print(data)

# data和new_data合为一张表,合并函数有concat(纵向或横向拼接)concat([ ,])和merge(主键合并)
# df2 = pd.merge(new_data,data)
# print(df2)

# 分组
price_df = pd.DataFrame({'区域':data['区域'].unique(),'总面积(㎡)':[0]*13})
# 总价格
sum_price = data['价格(元/月)'].groupby(data['区域']).sum()
# print(sum_price)
# 填充
price_df['总价格']=sum_price.values

# 总面积
sum_area = data['面积(㎡)'].groupby(data['区域']).sum()

# 填充
price_df['总面积(㎡)']=sum_area.values
print(price_df)
price_df['平均租金'] = round(price_df['总价格']/price_df['总面积(㎡)'],2)
print(price_df)

merge_df = pd.merge(new_data,price_df)
print(merge_df)

# 防止乱码
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

num = merge_df['房源数量']
price = merge_df['平均租金']
# print(num)

# x轴刻度
x = [i for i in range(13)]
# print(x)
# 数组转为列表方法to_list
labels = merge_df['区域']
print(labels)

# 画图
figure = plt.figure()   #

# 产生子图
ax1 = figure.add_subplot(111)
# 折线图,绘制平均租金
ax1.plot(x,price,'or-',label='价格')

# 折线图上的文字数据
for i,(_x,y) in enumerate(zip(x,price)):   # 函数enumerate用于遍历,i表示序列号
    plt.text(_x,y,price[i],color='black')

ax1.set_ylabel(['价格'])
ax1.legend(loc='upper left')
# 次坐标轴
ax2 = ax1.twinx()  # 产生一个ax1的镜面坐标
ax2.bar(x,num,color='green',alpha=0.3,label='数量')
ax2.legend(loc='upper right')
ax2.set_ylim([0,2000])
ax2.set_ylabel('数量')
plt.xticks(x,labels)  # 设置刻度的文字
plt.show()
