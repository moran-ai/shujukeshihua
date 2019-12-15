from matplotlib import pyplot as plt
import numpy as np

# 创建图形(也可以默认的图形)
# plt.figure(figsize=(10,10),facecolor='w')
# plt.show()
#
# # 保存
# # plt.savefig('路径')
#
# # 创建子图
# plt.subplot(2,1,1) #(行，列，子图编号)
# plt.plot([1,2,3,4],[1,2,3,4])
#
# plt.subplot(2,1,2)
# plt.plot([1,2,3,4],[1,2,3,4])
# plt.show()

# fig,ax=plt.subplots(2)#ax是一个包含2个axes对象的数组
# ax[0].plot([1,2,3,4], [1,2,3,4])
# ax[1].plot([4,3,2,1], [1,2,3,4])
# plt.show()

# import matplotlib
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['font.family']='sans-serif'

means_score = [12914 ,11826, 12997 ,12306.41 ,12327.28, 11406, 10608, 8378 ,
               8667.02 ,8052.78 ,6922.52 ,5744 ,4196, 4336, 4588 ,4751]
# y_labels = [12914 ,11826, 12997 ,12306.41 ,12327.28, 11406, 10608, 8378 ,
#                8667.02 ,8052.78 ,6922.52 ,5744 ,4196, 4336, 4588 ,4751]

# index = np.arange(16)
# bar_width = 0.4
# plt.bar(index, means_score, bar_width, color='#800080')
# # x_labels = [2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006,2005 ,2004,
# #             2003 ,2002, 2001 ,2000]
# x_labels = np.arange(2000,2016)
#
# # plt.yticks([4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,13500])
# # plt.yticks([4000,13500])
# plt.xticks(index,x_labels,rotation=45)   # rotation=45旋转45度
# # plt.xlim([0,6])  # x轴的范围
# plt.ylim([4000,13000])
# #plt.legend(loc='upper left')
# plt.show()

# 柱状图
# x = np.arange(2000, 2016)  # x轴的下标
# a = [12914, 11826, 12997, 12306.41, 12327.28, 11406, 10608,
# 8378, 8667.02, 8052.78, 6922.52, 5744, 4196, 4336, 4588, 4751]
# y = a[::-1]
# b = np.arange(4000, 13500, 1000)   # y轴刻度
# bar_width = 0.8   # 宽
# plt.bar(x, y, bar_width, alpha=1, color="#800080")  # 画柱状图
# plt.xticks(x, labels=x, rotation=45)  #
# plt.yticks(b)    # y轴的刻度
# plt.ylim(4000, 13500)   # y轴的范围

# # plt.savefig("picture/step1/fig1.png")
# plt.show()

# xstring1 = '2015, 2014, 2013, 2012, 2011,	 \
#            2010, 2009, 2008 ,2007 ,2006,	 \
#            2005 ,2004, 2003, 2002, 2001,	2000' #x轴标签

n = 6
ystring = ['']*n #y轴对应的6组数据
ystring[0] = '6793	6324	6237	5790.99	5357.1	5032	4681	3800	3863.9	3366.79	3167.66	2778	2359	2250	2170	2112'
ystring[1] = '6473	5933	5850	5429.93	4993.17	4725	4459	3576	3645.18	3119.25	2936.96	2608	2197	2092	2017	1948'
ystring[2] = '15157	12965	12591	11460.19	10993.92	10934	9662	7801	7471.25	6584.93	5833.95	5576	4145	4154	4348	4288'
ystring[3] = '12914	11826	12997	12306.41	12327.28	11406	10608	8378	8667.02	8052.78	6922.52	5744	4196	4336	4588	4751'
ystring[4] = '9566	9817	9777	9020.91	8488.21	7747	6871	5886	5773.83	5246.62	5021.75	3884	3675.14	3488.57	3273.53	3260.38'
ystring[5] = '4845	5177	4907	4305.73	4182.11	4099	3671	3219	3351.44	3131.31	2829.35	2235	2240.74	1918.83	2033.08	1864.37'

# labels = ['Commercial housing', 'Residential commercial housing',
#           'high-end apartments', 'Office Building', 'Business housing', 'Others'] #图例标签


# colors = ['#ff7f50', '#87cefa', '#DA70D6', '#32CD32', '#6495ED', '#FF69B4'] #指定颜色

'''
import numpy as np
import matplotlib.pyplot as plt
# A班计算机程序设计课5个小组的平均成绩柱状图
A_means_score = np.array([90, 85, 77, 82, 79])
# B班计算机程序设计课5个小组的平均成绩柱状图
B_means_score = np.array([67, 82, 87, 92, 95])
index = np.arange(5)
bar_width = 0.35
plt.bar(index, A_means_score, bar_width, # A班x轴数据起始位置为index序列
                alpha=0.4, color='b')
plt.bar(index+bar_width, B_means_score, bar_width, #B班x轴起始位置与A班数据错开
                alpha=0.4, color='r')
x_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
plt.xticks(index+bar_width/2, x_labels) # index+bar_width/2 使得标签居中显示

'''

'''
请编写代码绘制六类商品房平均销售价格柱状图，具体编程要求如下：

柱状图柱形宽度设置为0.8，颜色分别为列表colors中对应的RGB值；

横轴坐标轴范围为[-1,98]，第一组数据的柱形起始位分别为1,7,13,...91，间隔为6；

横轴标签为年份，从2000至2015，旋转角度为45度，标签位置位于6组数据正中间；

纵轴坐标轴范围为[1450, 15300]，轴刻度为2000,4000,...14000，刻度间隔为2000；

添加图例，图例标签如列表legend_labels所示，位置位于左上角；

添加标题'Selling Prices of Six Types of Housing'；

存储输出图像，图像名字为picture/step2/fig2.png。


'''
#x轴标签
# 并列柱状图
# xstring = '2015 2014 2013 2012 2011 2010 2009 2008 2007 2006' \
#            '	 2005 2004 2003 2002 2001	2000'
# xstring1 = xstring.split()
# xstring1.reverse()
#
# x = np.arange(1,n*len(xstring1),n)
# plt.xlim([-1,98])
# bar_wdith = 0.8
# for i in range(n):
#     y=ystring[i].split()
#     y.reverse()
#     y=[float(x) for x in y]
#     plt.bar(x+i*bar_wdith,y,bar_wdith,color=colors[i])
# plt.ylim([1450,15300])  # y轴范围
# plt.yticks(range(1450,15300,2000))   # y轴刻度
#
# plt.ylim([1450,15300])    # y轴范围
# plt.yticks(range(2000,15300,2000))     # 刻度
# plt.xticks(x+bar_wdith*2.5 ,xstring1,rotation=45)
# plt.legend(loc='upper left',labels=labels)  # 图例
# plt.title('Selling Prices of Six Types of Housing')
# # plt.show()

# 饼图

'''

matplotlib模块使用pie函数绘制饼图，其调用方式如下：

matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, 
autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1,
startangle=None, radius=None, counterclock=True, wedgeprops=None, 
textprops=None, center=(0, 0), 
frame=False, rotatelabels=False, *, data=None)[source]
请编写代码绘制育龄妇女的受教育程度分布饼图，具体编程要求如下：

突出教育程度为初中的楔形，偏移占比设为0.1 ；

饼图为等长等宽且有阴影；

楔形标签列表为['none', 'primary', 'junior', 'senior', 
'specialties', 'bachelor', 'master']；

楔形的颜色分别为['red','orange','yellow',
'green','purple','blue','black']；

请存储输出图像，图像名字为picture/step3/fig3.png。

import matplotlib.pyplot as plt
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs'] # 标签列表
sizes = [15, 30, 45, 10] # 绘制数据
explode = (0, 0.1, 0, 0)  # 只突出第二个切块，偏移比例为0.1 (i.e. 'Hogs')
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90) # shadow表示添加阴影，startangle表示旋转角度
plt.axis('equal')  # 用于显示为一个长宽相等的饼图
plt.show() #展示图像
'''

# labels= ['none', 'primary', 'junior', 'senior',
# 'specialties', 'bachelor', 'master']
# sizes = [2052380, 11315444, 20435242, 7456627, 3014264, 1972395, 185028]
# explode = (0, 0, 0.1, 0, 0, 0, 0)
# colors = ['red','orange','yellow','green','purple','blue','black']
# plt.pie(sizes,explode=explode,labels=labels,colors=colors,shadow=True)
# plt.axis('equal')  # 用于显示为一个长宽相等的饼图
# plt.show()

# 多子图绘制
'''
为了完成本关任务，你需要掌握：

设置画布大小；

绘制多个子图。

设置画布大小
matplotlib模块中采用figure函数设置自定义大小的画布，调用方式如下所示：

matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)[source]
在画图之前首先设置figure对象，使得后面的图形输出在这块规定了大小的画布上。参数num用于返回指定id的figure对象，如果此参数没有提供，则一个新的figure对象将被创建。参数figsize用于设置画布的宽高，单位为英尺。参数dpi用于设置分辨率。参数facecolor用于设置背景色，edgecolor用于设置边框颜色。

示例代码如下：

import matplotlib.pyplot as plt #导入matplotlib库
from math import sin, radians #导入数学计算库
x = range(0, 361)  #创建0-360的整数列表
y = [sin(radians(e)) for e in x] #获得x对应的正弦值，以列表存储
plt.figure(figsize=[8,5]) #在绘图之前设置画布大小，宽为8英尺，高为5英尺
plt.plot(x, y) #绘制曲线
plt.show()
绘制多个子图
在matplotlib中， 一个figure对象可以包含多个子图, 可以使用subplot()快速绘制, 其调用形式如下：

# 第一种：整个绘图区域被分成nrows行和ncols列，index表示第几个图
subplot(nrows, ncols, index, **kwargs) 
# 第二种：pos是三位数的整数，其中第一位是行数，第二位是列数，第三位是子图的索引
subplot(pos, **kwargs)
# 第三种：添加子图ax
subplot(ax)
subplot()的第二种调用方式的代码示例如下：

import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
plt.subplot(211) # 绘图区域被分为2行1列，接下来绘制第一幅图
plt.plot(t, s1)
ax2 = plt.subplot(212) # 绘制第二幅图
plt.plot(t, 2*s1)
plt.show()

请编写代码绘制图像，详细数据在右侧代码中已给出，具体编程要求如下：

包括两幅子图，左图是不同受教育程度育龄妇女生育子女的平均个数统计（按存活子女数统计），
右图是不同受教育程度育龄妇女生育子女的存活比例（即存活子女数/活产子女数）；

画布大小的宽高分别为14,5英尺；

两幅子图都需添加横轴标签，标签列表labels在右侧代码中已给出；

左图线条颜色设置为红色red，线性采用默认设置；

右图线条颜色设置为蓝色blue，线性采用默认设置；

请存储输出图像，图像名字为picture/step4/fig4.png。
'''
# import matplotlib
# matplotlib.use("Agg")

labels = ['none', 'primary', 'junior', 'senior', 'specialties', 'bachelor', 'master'] # 标签
womenCount = [2052380, 11315444, 20435242, 7456627, 3014264, 1972395, 185028]
birthMen = [2795259, 12698141, 13982478, 2887164, 903910, 432333, 35915]
birthWomen = [2417485, 11000637, 11897674, 2493829, 786862, 385718, 32270]
liveMen = [2717613, 12477914, 13847346, 2863706, 897607, 429809, 35704]
liveWomen = [2362007, 10854232, 11815939, 2480362, 783225, 384158, 32136]

#  请在此添加实现代码  #
# ********** Begin *********#
x = np.arange(len(labels))  # x轴数据
# print(x)
birth = np.array(birthMen)+np.array(birthWomen)   # 活产总人数
live = np.array(liveMen)+np.array(liveWomen)      # 存活总人数

# 设置画布为14，5
plt.figure(figsize=(14,5))

# 子图一，妇女生育子女的平均个数
plt.subplot(1,2,1)
a = (1.0*birth) / (1.0*np.array(womenCount))
# print(a)
plt.plot(x,a,'r')
plt.xticks(x,labels)    # x轴的刻度标签

# 子图二,子女的存活比列
plt.subplot(1,2,2)
b = (1.0*live) / (1.0*birth)* 100
plt.plot(x,b,'b')
plt.xticks(x,labels)   # x轴的刻度标签
plt.show()

# ********** End **********#
'''
x = np.arange(len(labels))
birth = np.array(birthMen) + np.array(birthWomen)
live = np.array(liveMen) + np.array(liveWomen)

plt.figure(figsize=[14,5]) #设置画布大小
plt.subplot(121)
birthrate = (1.0*live) / (1.0*np.array(womenCount))
plt.plot(x, birthrate, 'r')
plt.xticks(x, labels)

plt.subplot(122)
liverate = (1.0*live) / (1.0*birth) * 100
plt.plot(x, liverate, 'b')
plt.xticks(x, labels)
plt.show()'''

'''
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

labels = ['none', 'primary', 'junior', 'senior', 'specialties', 'bachelor', 'master'] # 标签
womenCount = [2052380, 11315444, 20435242, 7456627, 3014264, 1972395, 185028]
birthMen = [2795259, 12698141, 13982478, 2887164, 903910, 432333, 35915]
birthWomen = [2417485, 11000637, 11897674, 2493829, 786862, 385718, 32270]
liveMen = [2717613, 12477914, 13847346, 2863706, 897607, 429809, 35704]
liveWomen = [2362007, 10854232, 11815939, 2480362, 783225, 384158, 32136]

#  请在此添加实现代码  #
# ********** Begin *********
    
x = np.arange(len(labels))
birth = np.array(birthMen) + np.array(birthWomen)
live = np.array(liveMen) + np.array(liveWomen)

plt.figure(figsize=[14,5]) #设置画布大小
plt.subplot(1,2,1)
birthrate = (1.0*live) / (1.0*np.array(womenCount))
plt.plot(x, birthrate, 'r')
plt.xticks(x, labels)

plt.subplot(1,2,2)
liverate = (1.0*live) / (1.0*birth) * 100
plt.plot(x, liverate, 'b')
plt.xticks(x, labels)

plt.savefig('correct_picture/step4/correct_fig4.png')

'''
