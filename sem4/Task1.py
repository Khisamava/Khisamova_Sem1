import matplotlib.pyplot as plt

x1 = [0, 2.5, 4, 7, 9.5]
y1 = [0, 7.5, 12, 21, 28.5]

x2 = [1, 2.5, 4, 7, 9.5]
y2 = [4, 10, 16, 28, 38]

plt.figure(figsize=(8,5), dpi=100)
plt.plot(x1, y1, 'y^--', label='R1')
plt.title('U(I)', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.plot(x2, y2, 'g^--', label='R2')

plt.xlabel('X')
plt.ylabel('Y')

#Делаем график красивым!!!
#штрихи на осях
plt.xticks([0, 2, 4, 6, 8, 10, 12])
plt.yticks([0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])
plt.grid() #сетка по этим штрихам
plt.legend()

plt.show()