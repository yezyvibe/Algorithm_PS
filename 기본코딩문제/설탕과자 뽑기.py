h, w = list(map(int, input().split()))
n = int(input())
arr = [[0]*w for k in range(h)]

for i in range(n):
    l,d,x,y = list(map(int, input().split()))
    if d == 0:
        for j in range(l):
            arr[x-1][y-1+j] = 1
    else:
        for j in range(l):
            arr[x-1+j][y-1] = 1

for k in arr:
    print(' '.join(map(str,k)))