# coding:gbk
import matplotlib.pyplot as  plt
import pandas as pd
import numpy as np
crime = pd.read_csv('crimeRatesByState2005.csv')
# print(list(crime.murder))
crime2 = crime[crime.state != 'United States']
crime2 = crime2[crime2.state != 'District of Columbia']
# z = list(crime2.population)
z = list(crime2.population/10000)

# 数据为series 强转为list
colors = np.random.random(len(list(crime2.murder)))
# print(colors)

# 色图
cm = plt.get_cmap('RdYlBu')  # RdYlBu为图谱

plt.scatter(list(crime2.murder),list(crime2.burglary),s=z,c=z,cmap=cm,linewidths=1,alpha=1)
plt.xlabel('murder')
plt.ylabel('burglary')
plt.show()

