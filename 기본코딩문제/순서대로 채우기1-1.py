n = int(input())
arr = [[0]*n for i in range(n)]
x = 1

for i in range(n):
    for j in range(n):
        arr[i][j] = x
        x += 1
for a in arr:
    print(' '.join(map(str,a)))


