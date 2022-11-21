import sys


input = sys.stdin.readline
n, m = map(int, input().split())
times = []
answer = 0

for _ in range(n):
    times.append(int(input()))

times.sort()

start, end = 1, times[-1] * m

while start <= end:
    mid = (start + end) // 2

    possible = 0
    for time in times:
        possible += (mid // time)

    if possible >= m: # 검사할 사람 보다 더 많이 검사 -> 시간 줄여보기
        answer = mid
        end = mid - 1
    elif possible < m:
        start = mid + 1

print(answer)