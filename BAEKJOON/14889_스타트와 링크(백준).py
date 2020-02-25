import itertools
n = int(input())
bg = [list(map(int, input().split())) for l in range(n)]
arr = []

for i in range(1, n+1):
    arr.append(i)

com_lst = list(itertools.combinations(arr, n//2))
s_sum = []

if n // 2 >= 2:
    for com in com_lst:
        s_lst = []
        c_lst = list(com)
        combi = list(itertools.combinations(c_lst, 2))
        for x,y in combi:
            s = bg[x-1][y-1] + bg[y-1][x-1]
            s_lst.append(s)
        s_sum.append(sum(s_lst))

# 차이 구하기
gap_lst = []
for i in range(len(com_lst)):
    gap = abs(s_sum[i] - s_sum[-(i+1)])
    gap_lst.append(gap)
print(min(gap_lst))

