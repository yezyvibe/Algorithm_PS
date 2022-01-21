import sys

input = sys.stdin.readline
n, m, l = map(int, input().rstrip().split())
catch_cnt = [0]*n
catch_cnt[0] = 1
round = 0
idx = 0
while catch_cnt.count(m) == 0:
    round += 1
    if catch_cnt[idx] % 2 == 0:
        idx -= l
        if idx < 0:
            idx += n
        catch_cnt[idx] += 1
    else:
        idx += l
        if idx > n-1:
            idx -= n
        catch_cnt[idx] += 1
print(round)