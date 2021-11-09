import math

room = list(map(int, input()))
chk = [0] * 10

for i in room:
    chk[i] += 1

max_v = -1
tmp = 0
for i in range(10):
    if i == 6 or i == 9:
        tmp += chk[i]

    else:
        if chk[i] > max_v:
            max_v = chk[i]
tmp = math.ceil(tmp / 2)
if tmp > max_v:
    max_v = tmp
print(max_v)
