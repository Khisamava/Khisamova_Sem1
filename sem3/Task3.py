def Nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a+b)
a = int(input())
b = int(input())
d = Nod(a, b)
x = 1
y = (d - a*x)/b

while y != int(y):
    x -= 1
    y = (d - a * x) / b

x_min = x
y_min = y

for x in range(2, 100, 1):
   y = (d - a*x)/b
   while y != int(y):
       x -= 1
       y = (d - a * x) / b
   if (abs(x) + abs(y)) < (abs(x_min) + abs(y_min)):
       x_min = x
       y_min = y

print(x_min, y_min)
