A = list(map(int, input().split()))
for i in range (1, len(A)):
  A[-(i+1)], A[-i] = A[-i], A[-(i+1)]
print(A)
