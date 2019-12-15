# coding:gbk
import pandas as pd
import numpy as np

data = pd.read_csv("链家北京租房数据.csv",encoding='gbk')
print(len(data))
# print(pd.isnull(data).sum())  #统计空值数目
# print(data.isnull())  # 检测是否是空值
print(data.drop_duplicates(inplace=True))   #
# print(data.drop_duplicates(subset='对子列去重')
print(len(data))

# 统计价格总数
# print(data['价格(元/月)'].sum())

# 处理"面积(㎡)"这列的数据，例如59.11平方米转成59.11
df = data["面积(㎡)"].values   # 首先取出一列的值
# print(df)

# 字符串转为浮点数,使用一个for语句
d = []
for i in df:
    d.append(float(i[:-2]))
print(d)

# 放回原数据
data["面积(㎡)"] = d
print(data)

# 处理异常值,,使用函数replace()进行替换
df1 = data["户型"].values
# print(df1.replace('房间','室'))
# print(df1.replace('卫','厅'))

# 利用for循环
d1 = []
for s in df1:
    d1.append(s.replace('房间','室'))
    # d1.append(s.replace('卫','厅'))
print(d1)
# 放回原来的数据
data['户型'] = d1
print(data)

# 统计每个区域的房源总数量
"""
1.新建DataFrame,unique()表示去除重复
2.'房源数量':[0]*13 有13个区域，房价初始值为0
3.开始统计,进行分组
"""

new_data = pd.DataFrame({'区域':data['区域'].unique(),'房源数量':[0]*13})
print(new_data)

# 在原数据基础上进行分组,并统计详细信息、
group = data.groupby(by='区域').count()
print(group)

# 分组后的房源数量
new_data['房源数量'] = group.values
print(new_data)
new_data.sort_values("房源数量",ascending=False,inplace=True)
print(new_data)
# print(new_data['房源数量'].sort_values())

# 新建位置
data["位置"] = '北京市'+data['区域'].values+'区'+data["小区名称"].values
print(data)

import requests
import pandas as pd
import time
import json
class LngLat:
    # 获取位置一列的数据
    def get_data(self):
        house_names = data['位置']
        house_names = house_names.tolist()
        return house_names
    def get_url(self):
        url_temp = "http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=veWtxYB00rVDsxD7Oickyfdh5TlBe30F&callback=showLocation"
        house_names = self.get_data()
        return [url_temp.format(i) for i in house_names]
    # 发送请求
    def parse_url(self, url):
        while 1:
            try:
                r = requests.get(url)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
                continue
            return r.content.decode('UTF-8')
    def run(self):
        li = []
        urls = self.get_url()
        for url in urls:
            data = self.parse_url(url)
            str = data.split("{")[-1].split("}")[0]
            try:
                lng = float(str.split(",")[0].split(":")[1])
                lat = float(str.split(",")[1].split(":")[1])
            except ValueError:
                continue
            # 构建字典
            dict_data = dict(lng=lng, lat=lat, count=1)
            li.append(dict_data)
        f = open(r'经纬度信息.txt', 'w')
        f.write(json.dumps(li))
        f.close()
        print('正在写入...')
        print('写入成功')

if __name__ == '__main__':
    execute = LngLat()
    execute.run()
