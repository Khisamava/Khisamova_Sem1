with open('task9.txt', 'r') as f1:
    l1 = str(f1.read())
k = 1
print(l1)
stop_list = ['.', ',', '?', '!', ';']
for i in range(len(l1)-1):
    if l1[i] in stop_list:
        if l1[i+1] not in stop_list:
            k +=1

print(k)
