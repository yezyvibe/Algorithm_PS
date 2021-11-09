n = int(input())
arr= [[0]*n for l in range(n)]
cnt = 1

for i in range(n):
    for j in range(n):
        arr[i][j] = cnt
        cnt += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()