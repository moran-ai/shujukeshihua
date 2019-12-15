import pandas as pd
import numpy as np

data = pd.read_csv('guojia.csv')
# print(data)
# 自定义极差函数
def range_data_group(arr):
    return arr.max()-arr.min()

# 红酒极差
df = data.groupby(by='continent')['wine_servings'].agg(range_data_group)
# print(df)

# 啤酒总和
df1 = data.groupby(by='continent')['beer_servings'].agg(np.sum)
# print(df1)
df2 = pd.concat([df,df1],axis=1)
print(df2)
# df1 = df.agg({'wine_servings':[np.sum]})














