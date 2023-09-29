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

print(y)
print(isinstance(y, int))
while isinstance(y, int) != True:
    x -= 1
    y = (d - a * x) / b
res = f'{x, y, d}'
print(res)

