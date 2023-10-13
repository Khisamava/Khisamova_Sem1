import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10,5)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(211) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(212) # создали Axes ax2 в серии из 2 графиков, поставили на позицию [1,2] -- первый график во второй "строке" графиков

values1 = np.random.normal(0, 10, 10000)
ax1.hist(values1, color='m', bins=50)
ax1.grid() # делаем сетку на графике ax1

values2 = np.random.normal(0, 5, 1000)
ax2.hist(values2, bins = 50)
ax2.grid()

plt.show()