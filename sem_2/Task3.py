st = input()
l = len(st)
num_steps= l // 2
flag1 = True
flag2 = True
symmetric_letters = ['A', 'M', 'I', 'H', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']

for i in range(num_steps):
    if st[i] != st[-i-1]:
        flag1 = False
        break

for i in range(num_steps):
    if st[i] in symmetric_letters:
        if st[i] != st[-i-1]:
            flag2 = False
            break
    elif st[i] != symmetric_letters:
        flag2 = False
    if st[i] == 'E':
        if st[-i-1] == '3':
            flag2 = True;
    if st[i] == 'J':
        if st[-i-1] == 'L':
            flag2 = True;
    if st[i] == 'S':
        if st[-i-1] == '2':
            flag2 = True;
    if st[i] == 'Z':
        if st[-i-1] == '5':
            flag2 = True;
    if st[i] == '3':
        if st[-i-1] == 'E':
            flag2 = True;
    if st[i] == 'L':
        if st[-i-1] == 'J':
            flag2 = True;
    if st[i] == '2':
        if st[-i-1] == 'S':
            flag2 = True;
    if st[i] == '5':
        if st[-i-1] == 'Z':
            flag2 = True;



res = f'{st} palindrom = {flag1}'
res1 = f'{st} mirror line = {flag2}'
print(res)
print(res1)
if flag1 == True and flag2 == True:
    res2 = f'{st} is a mirrored palindrom '
    print(res2)
elif flag1 == False or flag2 == False:
    res3 = f'{st} is NOT a mirrored palindrom'
    print(res3)



