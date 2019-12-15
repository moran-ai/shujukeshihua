# Series数据结构的重新索引
# 创建一个简单的Series
import pandas as pd
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d','b','a','c'])
# print(obj)

# 更改索引 reindex
obj1 = obj.reindex(['a','b','c','d','e'])
# print(obj1)

# 填充缺失值  使用fill_value=0填充
obj2= obj.reindex(['a','b','c','d','e'],fill_value=0)
# print(obj2)

# 使用ffill进行前项值填充
obj3 = obj.fillna(method='ffill')
# print(obj3)

obj4 = obj1.fillna(method='bfill')
# print(obj4)
