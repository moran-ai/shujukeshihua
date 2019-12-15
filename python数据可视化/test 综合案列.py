# coding:gbk
import pandas as pd
import numpy as np

data = pd.read_csv("���ұ����ⷿ����.csv",encoding='gbk')
print(len(data))
# print(pd.isnull(data).sum())  #ͳ�ƿ�ֵ��Ŀ
# print(data.isnull())  # ����Ƿ��ǿ�ֵ
print(data.drop_duplicates(inplace=True))   #
# print(data.drop_duplicates(subset='������ȥ��')
print(len(data))

# ͳ�Ƽ۸�����
# print(data['�۸�(Ԫ/��)'].sum())

# ����"���(�O)"���е����ݣ�����59.11ƽ����ת��59.11
df = data["���(�O)"].values   # ����ȡ��һ�е�ֵ
# print(df)

# �ַ���תΪ������,ʹ��һ��for���
d = []
for i in df:
    d.append(float(i[:-2]))
print(d)

# �Ż�ԭ����
data["���(�O)"] = d
print(data)

# �����쳣ֵ,,ʹ�ú���replace()�����滻
df1 = data["����"].values
# print(df1.replace('����','��'))
# print(df1.replace('��','��'))

# ����forѭ��
d1 = []
for s in df1:
    d1.append(s.replace('����','��'))
    # d1.append(s.replace('��','��'))
print(d1)
# �Ż�ԭ��������
data['����'] = d1
print(data)

# ͳ��ÿ������ķ�Դ������
"""
1.�½�DataFrame,unique()��ʾȥ���ظ�
2.'��Դ����':[0]*13 ��13�����򣬷��۳�ʼֵΪ0
3.��ʼͳ��,���з���
"""

new_data = pd.DataFrame({'����':data['����'].unique(),'��Դ����':[0]*13})
print(new_data)

# ��ԭ���ݻ����Ͻ��з���,��ͳ����ϸ��Ϣ��
group = data.groupby(by='����').count()
print(group)

# �����ķ�Դ����
new_data['��Դ����'] = group.values
print(new_data)
new_data.sort_values("��Դ����",ascending=False,inplace=True)
print(new_data)
# print(new_data['��Դ����'].sort_values())

# �½�λ��
data["λ��"] = '������'+data['����'].values+'��'+data["С������"].values
print(data)

import requests
import pandas as pd
import time
import json
class LngLat:
    # ��ȡλ��һ�е�����
    def get_data(self):
        house_names = data['λ��']
        house_names = house_names.tolist()
        return house_names
    def get_url(self):
        url_temp = "http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=veWtxYB00rVDsxD7Oickyfdh5TlBe30F&callback=showLocation"
        house_names = self.get_data()
        return [url_temp.format(i) for i in house_names]
    # ��������
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
            # �����ֵ�
            dict_data = dict(lng=lng, lat=lat, count=1)
            li.append(dict_data)
        f = open(r'��γ����Ϣ.txt', 'w')
        f.write(json.dumps(li))
        f.close()
        print('����д��...')
        print('д��ɹ�')

if __name__ == '__main__':
    execute = LngLat()
    execute.run()
