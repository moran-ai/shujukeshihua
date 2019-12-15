import pandas as pd
df = pd.read_csv('huizong.csv',encoding='utf-8')
# print(df)

# 获取品牌和评论
# print(df.loc[:,["品牌",'评论']])

#  得到电热器品牌为'’美的'的所有评论数据
# print(df.loc[df['品牌']=='美的',:])
# print(df.loc[df['品牌']=='美的','评论'])

# 使用iloc切片方式获取品牌和评论两列数据
print(df.iloc[:,[4,5]])
print(df.iloc[:,4:6])

