# import numpy as np
# from PIL import Image
# im = np.array(Image.open("tianxinge.png"))
# print(im)
# print(im.shape)
# print(type(im))
#

# # 一维数组
# # a = np.array([1, 2, 3, 4])
# # print(a)
# # print(type(a))
#
#

import pandas as pd
# index = a.split(',')
# element = b.split(',')
# data = pd.Series(element,index)
# print(data)
# 创建dataframe对象
#
# data1 = pd.DataFrame([[1,2,3],[4,5,6]],index=['a','b'],columns=['name','age','score'])
# print(data1)
#
# data3 = pd.Series("元素", "index")
# data4 = pd.Series("元素","index")
# data5 = pd.DataFrame({"first":data3,"second":data4})
# data = [{'a': i, 'b': 2 * i} for i in range(3)]
# print(pd.DataFrame(data))

# 第一种方式数组创建Dataframe对象
data = pd.DataFrame([['一年级',25,15],['二年级',25,15],['三年级',25,15],['四年级',25,15]],
columns=['班级','男生人数','女生人数'])
# print(data)

# 第二种方式series方式创建
data1 = pd.Series(['一年级','二年级','三年级'])
data2 = pd.Series([25,25,25])
data3 = pd.Series([15,15,15])
data4 = pd.DataFrame({'班级':data1,'男生人数':data2,'女生人数':data3})
print(data4)

data5 = pd.DataFrame({'班级':['一年级','二年级','三年级'],'男生人数':[25,25,25],
                      '女生人数':[15,15,15]})
# print(data5)

# a = pd.read_csv('运动员信息表.csv')
# csv 分割符文件
