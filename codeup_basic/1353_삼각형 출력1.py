n = int(input())
arr= [[0]*n for l in range(n)]

for i in range(n):
    for j in range(i,n):
        arr[i][j]= '*'

for i in range(n):
    for j in range(n):
        if arr[i][j]== 0:
            arr[i][j] = ' '

for a in arr:
    print(''.join(map(str, a)))