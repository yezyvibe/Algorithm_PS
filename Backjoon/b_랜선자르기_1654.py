import sys

def binary_search(mid, cables):
    count = 0
    for cable in cables:
        count += (cable // mid)
    return count

input = sys.stdin.readline
k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]
cables.sort()

start = 1
end = cables[-1]

while start <= end:
    mid = (start + end) // 2
    res = binary_search(mid, cables)

    if res >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)