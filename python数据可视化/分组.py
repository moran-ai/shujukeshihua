import pandas as pd
import numpy as np
df = pd.read_csv('地区信息.csv',encoding='gbk')
# print(df)

# 分组
df1 = df.groupby('省级单位')
# print(df1)

# 遍历分组
# for i in df1:
#      print(i)

# 第二种方法取得每组数据
data = dict([i for i in df1])['北京']  # 列表推导式  ,dict创建一个字典
# print(data)

# 统计
# df1 = df.groupby('省级单位'.max())

data_frame=pd.DataFrame(np.arange(36).reshape((6,6)),columns=list('abcdef'))
data_frame['key']=pd.Series(list('aaabbb'),name='key')  # 添加数据
#分组
data_group=data_frame.groupby('key')
#使用agg方法聚合
print(data_group.agg(np.sum))
