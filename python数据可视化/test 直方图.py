# coding:gbk
import numpy as np
import pandas as pd
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False
# titanic = pd.read_csv('ds')

img = cv.imread('cat.png')
imggray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# plt.imshow(imggray,cmap=plt.cm.gray)
hist = cv.calcHist([img],[0],None,[256],[0,125])
plt.figure()
plt.title('grayhist')
plt.xlabel('bins')
plt.ylabel('fixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
