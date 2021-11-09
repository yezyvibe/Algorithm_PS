arr = [[0]*10 for i in range(10)]


for i in range(4) :
    num = list(map(int, input().split()))
    a,b,c,d = num
    for k in range(a,c):
        for j in range(b,d):
            arr[k][j] = 1

    i_cnt = 0
for i in arr:
    i_cnt += i.count(1)

print(arr)
print(i_cnt)