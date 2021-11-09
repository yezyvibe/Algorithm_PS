n = int(input())
m = int(input())
arr = [[0]*m for i in range(n)]
cnt = n*m 

for i in range(n):
    for j in range(m):
        arr[i][j] = cnt
        cnt -= 1
print(arr)