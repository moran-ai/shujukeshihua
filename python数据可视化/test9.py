import pandas as pd

df = pd.read_csv('北京地区信息.csv',encoding='gbk')
df1 = pd.read_csv('天津地区信息.csv',encoding='gbk')
df2 = pd.concat([df,df1])
# print(df2)
print(df2.to_csv('信息.csv'))
