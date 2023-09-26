s = input().split()
G = int(s[0])
st = s[1]

L = len(st)
num = L // G
A = []
for i in range(num):
    A.append(st[i*G:(i+1)*G])
# print(A)
for j in range(len(A)):
    word = A[j]
    word_reserved = word[::-1]
    print(word_reserved)
