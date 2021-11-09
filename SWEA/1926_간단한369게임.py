n = int(input())
ori = []
cnt_lst = []
for j in range(1,n+1):
    ori.append(j)

for i in range(1,n+1):
    a = str(i)
    cnt = 0
    for k in range(len(a)):
        b = a[k]
        if b == '0':
            pass
        elif int(b) % 3 == 0:
            cnt += 1

    cnt_lst.append(cnt)
for i in range(n):
    if cnt_lst[i] == 0:
        pass
    elif cnt_lst[i] >= 1:
        ori[i] = '-'*cnt_lst[i]

print(' '.join(map(str,ori)))