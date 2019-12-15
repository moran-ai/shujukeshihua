import pandas as pd
# 读取csv文件
df = pd.read_csv('地区信息.csv',encoding='gbk')
# print(df)
# print(df.shape)

# obj = pd.DataFrame(df)
# 检测空值
# print(pd.isnull(obj).sum())   # sum函数统计有多少空值

# print('*'*50)

# 检测非空值的数目
# print(pd.notnull(obj).sum())   # sum函数统计有多少非空值

# 处理空值
'''pandas.DataFrame.dropna(self,axis=0,how='any',thresh=None,subset=None,inplace=Flase)
axis:确定过滤的行或列，默认为0，默认删行
how：确定过滤的标准,取值标准:
any:默认值，如果存在Nan值，则删除该行该列
all:如果所有的值都是Nan,则删除该行或该列
thresh 阈值'''

# 删除法处理
len1 = len(df)
df.dropna(axis=0,inplace=True)
len2 = len(df)
# print('删除后的条数是：',len1-len2)

# 替换法
'''
缺失值为数值型时，用均值，中位数，众数填充
缺失值为类别型时，用众数填充
pd.DataFrame.fillna
'''

# 填充缺失值
# 求平均值
df1 = df.loc[:,['常住人口（万人）']]
df2 = round(df1.mean(),2)  # mean() 平均数函数
# round 四舍五入函数,round(number)，number保留几位数
# print(df2)
# df.fillna(df2,inplace=True)
# df.to_csv('新地区信息.csv')
# print(df)

# 重复值的检测和处理
# pd.DataFrame.drop_duplicates()  只对DateFrame和Series有效
# print(df.duplicated())  # 结果为True说明有重复值存在
# 做去重处理
len3 = len(df)
print(df.drop_duplicates(inplace=True))
print('删除了',len3-len(df),'重复值')

