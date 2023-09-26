A = list(map(int, input().split()))
A_max = A[0]
max_count = A.count(max)

for i in A:
    if A.count(i) > max_count:
        A_max = i
        max_count = A.count(i)

print(A_max)