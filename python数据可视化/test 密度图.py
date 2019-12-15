# coding:gbk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# import numpy as np
# from matplotlib import pyplot as plt
# import seaborn as sns
fig,ax=plt.subplots()

np.random.seed(4) #设置随机数种子
Gaussian=np.random.normal(0,1,1000) #创建一组平均数为0，标准差为1，总个数为1000的符合标准正态分布的数据
ax.hist(Gaussian,bins=25,histtype="stepfilled",normed=True,alpha=0.6)
sns.kdeplot(Gaussian,shade=True)

plt.show()
