import pandas as pd
import numpy as np

# isnull,pandas.isnull(obj)，只有一个参数，表示检查空值的对象.
obj = pd.Series([1,None,np.NAN])
print(pd.isnull(obj))

# pandas.notnull(obj) 检测非空值
obj = pd.Series([1,None,np.NAN])
print(pd.notnull(obj))

# 结合sum函数，统计有多少空值和非空值

# 处理空值
# pandas.DataFrame.dropna(self,axis=0,how='any',thresh=None,subset=None,inplace=Flase)
# axis:确定过滤的行或列，默认为0，默认删行
# how：确定过滤的标准
