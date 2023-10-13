import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris_data.csv')
A = list(df['Species'])
setosa = 0
virginica = 0


for i in range (len(A)):
    if A[i] == 'Iris-setosa':
        setosa += 1

    elif A[i] == 'Iris-virginica':
        virginica += 1

plt.figure(0)
plt.pie([setosa, virginica], labels = ['Iris-setosa', 'Iris-virginica'])
plt.title('Species')

B = list(df['PetalLengthCm'])
a = 0
b = 0
c = 0
print(B)
for j in range(len(B)):
    if B[j] < 1.2:
        a += 1
    elif B[j] > 1.2 and B[j] < 1.5:
        b += 1
    elif B[j] > 1.5:
        c += 1
print(a, b, c)
plt.figure(1)
plt.pie([a, b, c], labels=['<1.2', '>1.2 and <1.5', '>1.5'])
plt.title('PetalLengthCm')

plt.show()
