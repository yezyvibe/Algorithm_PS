arr = [1,2,3]
N = len(arr)
cnt = 0

for i in range(8):
    sub = []
    SUM = 0
    for j in range(3):
        if i & (1<<j):
            sub.append(arr[j])
    for x in range(len(sub)):
        SUM += sub[x]
    if SUM == 0:
        cnt +=1
print(cnt)