import pandas as pd
from sklearn import datasets

'''def demo1():
    iris = datasets.load_iris().data    # 鸢尾花数据集，返回的是array
    df = iris[:30]
    print(df)
    df1 = pd.DataFrame(df,columns=('a','b','c''d'))
    print(df1-df1.iloc[0])   # 最后一行减去第一行的值'''

iris = datasets.load_iris().data
# print(iris)
df = pd.DataFrame(iris,columns=('a','b','c','d'))
# print(df[:30])
# print(df.iloc[:30])
df1 = df.iloc[:30]
# print(df1-df1.iloc[0])
print(df1.subtract(df1.iloc[0:]))
