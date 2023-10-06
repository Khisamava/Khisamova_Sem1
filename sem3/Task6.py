import numpy as np
tx = [1, 2, 3, 4, 5]
ty = [2*i + 1 for i in tx]
n = 5
x = np.array(tx)
y = np.array(ty)
x_mean = np.mean(x)
y_mean = np.mean(y)
numerator = (x - x_mean)*y
denominator = (x - x_mean)**2
a = np.sum(numerator)/np.sum(denominator)
b = y_mean - a*x_mean
Dyy = np.sum((y - y_mean)**2)
Dxx = np.sum((x-x_mean)**2)
O_a = np.sqrt(1/n-2*(Dyy/Dxx-a**2))
O_b = O_a*np.sqrt(np.sum(x_mean**2))
print(a, b, O_a, O_b)



