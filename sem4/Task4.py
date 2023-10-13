import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris_data.csv')
x1 = list(df['SepalLengthCm'])
y1 = list(df['SepalWidthCm'])
x2 = list(df['PetalLengthCm'])
y2 = list(df['PetalWidthCm'])

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

ax1.plot(x1, y1, 'y^', label='Sepal')
ax1.grid()
ax2.plot(x2, y2, 'r^', label='Petal')
ax2.grid()
ax3.plot(x1, y2, 'b^')
ax3.grid()
ax4.plot(x2, y1, 'm^')
ax4.grid()

plt.show()  #не думаю что этот странный набор точек можно аппроксимировать чем то,
# выглядит как полностью рандомный набор точек
