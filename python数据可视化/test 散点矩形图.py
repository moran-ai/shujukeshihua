# coding:gbk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ����ȫ���ͻ�ʢ������
crime = pd.read_csv('crimeRatesByState2005.csv')
crime2 = crime[crime.state != 'United States']
crime2 = crime2[crime2.state != 'District of Columbia']
crime2 = crime2.drop(['state'],axis=1)
crime2 = crime2.drop(['population'],axis=1)

# pairplot������
# 1.����ΪDataFrame
# 2.�Խ���
g = sns.pairplot(crime2,diag_kind='kde')
plt.show()


