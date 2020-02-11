n = int(input())
arr= []
for l in range(1,n+1):
    arr.append([0]*l)

for k in range(n):
    arr[k][0] = int(input())

for i in range(1,n):
    for j in range(1,len(arr[i])):
        arr[i][j] = arr[i][j-1] - arr[i-1][j-1]

for a in arr:
    print(' '.join(map(str, a)))
