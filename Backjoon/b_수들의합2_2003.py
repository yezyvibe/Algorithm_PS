import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
s_idx, e_idx = 0, 1
cnt = 0
while e_idx <= n and s_idx <= e_idx:
    sum_arr = sum(arr[s_idx:e_idx]) 
    if sum_arr == m:
        cnt += 1
        e_idx += 1
    if sum_arr >= m:
        s_idx += 1
    elif sum_arr < m:
        e_idx += 1
print(cnt)