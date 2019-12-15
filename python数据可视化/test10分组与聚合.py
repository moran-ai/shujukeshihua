import pandas as pd
import numpy as np

data = pd.read_csv('附件.csv',encoding='gb2312')
# print(data)
# print(data.dtypes)
# print(data.notnull().sum()) # 检测不是空值
# print(data.isnull().sum())   # 是否空值
# 是否有缺失值
# print(data.info())

# 删除空值
print(data.dropna(inplace=True))  # inplace=True 对于原数据生效
# print(data.shape)

# 删除重复值
print(data.drop_duplicates(inplace=True))
#print(data.shape)

# 处理异常值
data['销售金额'] = round(data['销售数量']*data.loc[:,'商品单价'],2) # round四舍五入
# print(data['销售金额'])

# 统计大类中商品销售金额
# print(data['大类名称'].value_counts()) # value_counts统计值的数目

# 方法一
group = data.groupby(by='大类名称')['销售金额'].sum() # 求销售金额的总和
# print(group)

# 方法二
group1 = data.groupby(by='大类名称')['销售金额'].agg(np.sum)
# print(group1)

# 求极差
# 自定义极差值函数
def range_data_group(arr):
    return arr.max() - arr.min()
group2 = data.groupby(by='大类名称')['销售金额'].agg(range_data_group)

# print(group2)

# 不同的列
dict = {'销售数量':[np.max],'销售金额':[np.mean]}
group3 = data.groupby(by='大类名称').agg(dict)
print(group3)

# for i,j in group:  # i 每组的组名,比如：'休闲',’文体'
#     print(i,j)     # j 元素

# def sub(df):
#     max = df['wine_servings'].groupby(df['continent']).max()
#     min = df['wine_servings'].groupby(df['continent']).min()
#     wine = max -min
#     beer = df['beer_servings'].groupby(df['continent']).sum()
#     return wine,beer
#
# def main():
#     df = pd.read_csv('guojia.csv')
#     wine,beer = sub(df)
#     result = pd.concat([wine,beer],axis=1)
#     return result
# main()

df = pd.DataFrame([[2,3],]*3,columns=['A','B']).apply(lambda x:x+1)
# print(df)
# lambda 匿名函数
# apply 应用
# print((pd.DataFrame([[2,3],]*3,columns=['A','B'])).apply(lambda x:x+1))
