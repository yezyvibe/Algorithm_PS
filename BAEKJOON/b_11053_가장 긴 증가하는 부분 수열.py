import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = [1] * n

for i in range(1, n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            cnt[i] = max(cnt[i], cnt[j] + 1)

print(max(cnt))
