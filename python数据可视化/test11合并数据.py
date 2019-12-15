import pandas as pd

# 读取三个csv文件
df = pd.read_csv('state-abbrevs.csv')
df1 = pd.read_csv('state-ares.csv')
df2 = pd.read_csv('state-population.csv')

# print(df2.head())
# print(df1.head())
# print(df.head())

# 合并pop和abbrevs并删除重复列
df3 = pd.merge(df,df1)
# print(df3)
# print(df3.drop_duplicates('abbreviation'))
# 去重
# 填充对应的全称

# 合并面积数据
areas = pd.merge('areas',on='state',how='lefter')
# print(areas)
# 删掉这些缺失值
# drop
# 取year为2010年的数据，并将索引设为state列
# reindex
# 计算人口密度

# 对密度求和

# 对值进行排序
# df3.sort_values('')
# 输出人口密度前5名和倒数5名
# head()
# tail

