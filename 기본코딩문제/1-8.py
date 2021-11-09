n, m = list(map(int, input().split()))
arr = [[0]*m for k in range(n)]
x = 1
for i in range(m):
    for j in range(n):
        arr[j][m-1-i] = x
        x += 1

for a in arr:
    print(' '.join(map(str, a)) )