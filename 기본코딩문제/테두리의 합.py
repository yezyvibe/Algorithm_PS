n = int(input())
arr = [[0]*n for l in range(n)]
cnt = 1
sumLst = []
for i in range(n):
    for j in range(n):
        arr[i][j] = cnt
        cnt += 1

for k in range(n):
    sumLst.append(arr[0][k])
    sumLst.append(arr[k][0])
    sumLst.append(arr[n-1][k])
    sumLst.append(arr[k][n-1])

a = set(sumLst)
print(sum(a))


