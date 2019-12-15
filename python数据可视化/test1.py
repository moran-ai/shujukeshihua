# loc['行索引名称或条件','列索引名称']

# import pandas as pd
# df = pd.read_csv('运动员信息表.csv',encoding='gbk')
# print(df)
# print(type(df))
# print(df.size)
# print(df.shape)
# print(help(pd.read_csv))

# 需要前5行数据
# print(df.head())  # 不填数字默认前五条数据
#
# # 后五条数据
# print(df.tail())  # 不填数字默认后五条数据

# 选出姓名
# print(df['姓名'])

# 选出所有的出生年月
# print(df.loc[:,'出生年份（年）'])

# 选出所有的姓名和出生年月这两列数据
# print(df.loc[:,['出生年份（年）','姓名']])

# 选出姓名和出生年月这两列数据前五行数据
# print(df.loc[:4,['出生年份（年）','姓名']])
# # print(df.loc[:,['出生年份（年）','姓名']].head())

# 选出运动员体重大于75kg的姓名
# a = df['体重(kg)']
# print(df.loc[a>75,['姓名']])
#
# print(df.loc[df['体重(kg)']>75,:])
# print(df.loc[df['体重(kg)']>75,'姓名'])

# iloc['行索引位置','列索引位置']

# 使用iloc选出姓名
# print(df.iloc[:,0])

# 使用iloc选出姓名和性别
# print(df.iloc[:,[0,1]])

# 使用iloc选出'姓名和性别'前两行
# print(df.iloc[0:2,[0,1]])

# 在DataFrame中新增一列
# df['身价'] = 100000
# print(df)
# df.to_csv('新体重运动员.csv')  # 存进csv文件

# area = pd.Series({'California': 423967, 'Texas': 695662, 'New York': 141297,
#                   'Florida': 170312, 'Illinois': 149995})
# pop = pd.Series({'California': 38332521, 'Texas': 26448193,
#                  'New York': 19651127, 'Florida': 19552860, 'Illinois': 12882135})
# data = pd.DataFrame({'area':area, 'pop':pop})
# print(data)
# #增加一列数据
# data['人口密度']=data['pop']/data['area']
# print(data)

# 删除某行或某行数据 drop
# axis为0表示删除行，为1表示删除列,默认删除行
# # inplace 代表操作对原数据是否生效
# area = pd.Series({'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995})
# pop = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860, 'Illinois': 12882135})
# data = pd.DataFrame({'area':area, 'pop':pop})
# # print(data)
# #增加一列数据
# data['人口密度']=data['pop']/data['area']
# print(data)
#
# # data时DataFrame对象
# # 删除人口密度的数据
# data.drop(labels='人口密度',axis=1,inplace=True)   # axis=1 删除列
# # label行索引名或者列索引名
# # inplace=True 对原数据生效
# print(data)

import pandas as pd
import numpy as np

arr = input(':')
dates = pd.date_range('20190101', periods=25) # 生成时间序列
df = pd.Series(eval(arr),index=dates)

# print(dates)
# print(df)
# print(dates.loc[dates['periods']>100,'20190101'])
str = pd.to_datetime('2019-01-29')
df[str]=320
# print(df)
df = df[3:]
print(df[df>100])

# str1 = pd.to_datetime('2019-01-02')
# str2 =  pd.to_datetime('2019-01-03')
# print(df[(df>str1) & (df>str2)])
# [4,9,4,3,1,981,13,6,46,1,647,64,31,46,46,13,198,76,13,1698,7496,2,100,8201,30])
# [55,524,413,1,9481,13,65,46,1,7,64,51,46,490,13,198,76,134,168,74,2,101,82,309,3210]
