size = int(input())
symbol = input()
for i in range(size+1):
    print(symbol*i)
    i+=1
j = size-1
while j != 0:
    print(symbol*j)
    j -= 1