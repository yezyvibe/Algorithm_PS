n = int(input())
arr = [[0]*n for i in range(n)]
a = 0

for i in range(n):
    for j in range(n):
        a += 1
        arr[i][j+(n-1-2*j)*(i%2)] = a

print(arr)
