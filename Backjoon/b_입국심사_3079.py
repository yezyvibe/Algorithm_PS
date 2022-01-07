import sys


# mid는 검사에 소요되는 시간
def binary_search():
    start, end = judging_table[0], judging_table[-1] * m
    min_v = judging_table[-1] * m
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in range(n):
            total += mid // judging_table[i]
        if total >= m:
            end = mid - 1
            min_v = min(min_v, mid)
        else:
            start = mid + 1
    return min_v

input = sys.stdin.readline
n, m = map(int, input().split())
judging_table = [int(input()) for _ in range(n)]
judging_table.sort()
print(binary_search())