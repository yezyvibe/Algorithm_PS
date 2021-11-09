ARR = [int(x) for x in input()]
CNT = [0]*10
# print(CNT)

for i in range(len(ARR)):
    n = ARR[i]
    CNT[n] += 1
    print(CNT)

i = 0
triple = 0
run = 0

while i < len(CNT):
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue;

    if c[i] >= 1 and c[i+1] >=1 and c[i+2] >= 1
        run += 1

    i = i + 1

if  # tri + run == 2
