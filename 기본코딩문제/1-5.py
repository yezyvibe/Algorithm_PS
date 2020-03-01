n, m = list(map(int, input().split()))
arr = [[0]*m for k in range(n)]
x = 1
for i in range(n):
    for j in range(m):
         arr[n-1-i][m-1-j] = x
         x += 1
for a in arr:
    print(' '.join(map(str,a)))