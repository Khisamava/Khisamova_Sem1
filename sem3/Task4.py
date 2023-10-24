size = float(input())
symbol = input()
Size = int(size/2+1)
for i in range(Size+1):
    print(symbol*i)
    i+=1
j = Size-1
while j != 0:
    print(symbol*j)
    j -= 1