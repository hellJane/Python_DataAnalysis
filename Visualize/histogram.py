import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

'''
本节介绍如何画直方图，matplotlib中三种主要的图形，第一个是plot，即直线，第二个是scatter，即散点图，第三个是histogram，直方图

-> plot根据(X, Y)来绘制一个一个的点，然后连成直线，当点足够多时，看上去就是一条光滑的曲线
-> scatter的输入也是长度相等的(X, Y)，但只画出一个个的散点，不连成线
-> histogram的输入比较奇怪，它的输入是一个数组X，然后一个整数或者数组bins，bins用于划分数组X，
        1. 如果是整数，则根据数组X中的最大值和最小值，给数组X均分成bins个区间段；
        2. 如果是一个数组，则根据每相邻的两个数值，划分成数组长度减一个区间段。
   最后返回一个bins数组，这个数组的长度是输入的bins+1,每两个之间就是一个区间段，
   然后图形中的y轴，就表示每个区间内包含的X的个数或者概率密度函数。

for example:  if bins is: [1, 2, 3, 4]
              then the first bin is [1, 2) (including 1, but excluding 2) and the second [2, 3).
              The last bin, however, is [3, 4], which includes 4.

matplotlib.pyplot.histogram docs: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist
'''

X = [1, 2, 1]
bins = [0, 1, 2, 3]
# 落入[0, 1)区间中的有零个，[1, 2)中的有两个1，[2, 3]中的有一个2
# 所以hist数组为[0, 2, 1]
hist, bins = np.histogram(X, bins)
print('X: ', X)
print('bins: ', bins)
print('hist & bins generated by np.histogram(X, bins): ', hist, bins)
hist, bins = np.histogram(X, bins, density=True)  # 此时hist中的数值是概率而不是个数了
print('hist(density probability) & bins generated by np.histogram(X, bins): \n', hist, bins)

X = np.arange(10)
bins = 3    # 三等分数组X
hist, bins = np.histogram(X, bins)
print('X: ', X)
print('bins: ', bins)
print('hist & bins generated by np.histogram(X, bins): ', hist, bins)

np.random.seed(0)

# example data
mu = 100       # mean of distribution
sigma = 15     # standard deviation of distribution
# ** 这是个非常有用的方法，用于生成服从正态分布(mu, sigma**2)的数据 ** #
x = mu + sigma * np.random.randn(437) 

num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
# 此处normed=1等于上面的density=True
# rwidth表示填充每个bar的百分比，0.9能让边界更清晰
n, bins, patches = ax.hist(x, num_bins, normed=1, rwidth=0.9) 

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
