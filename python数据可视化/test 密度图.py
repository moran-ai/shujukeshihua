# coding:gbk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# import numpy as np
# from matplotlib import pyplot as plt
# import seaborn as sns
fig,ax=plt.subplots()

np.random.seed(4) #�������������
Gaussian=np.random.normal(0,1,1000) #����һ��ƽ����Ϊ0����׼��Ϊ1���ܸ���Ϊ1000�ķ��ϱ�׼��̬�ֲ�������
ax.hist(Gaussian,bins=25,histtype="stepfilled",normed=True,alpha=0.6)
sns.kdeplot(Gaussian,shade=True)

plt.show()
