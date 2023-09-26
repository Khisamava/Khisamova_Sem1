A = list(map(int, input().split()))
for i in A:
    if A.count(i) == 1:
        print(i)