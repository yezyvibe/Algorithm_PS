num_str = input()

res = 0
tmp = ''
chk = 0
for i in range(len(num_str)):
    a = num_str[i]
    if a.isdigit() and chk == 0:
        tmp += a
    elif a == '-' and chk == 0:
        chk = 1
        res += int(tmp)
        tmp = ''
    elif a == '+' and chk == 0:
        res += int(tmp)
        tmp = ''
    elif a.isdigit() and chk == 1:
        tmp += a
    else:
        res -= int(tmp)
        tmp = ''
if '-' in num_str:
    res -= int(tmp)
else:
    res += int(tmp)

print(res)