import sys

def binary_search(arr, target):
    # target은 개똥벌레가 지나가는 구간, 기준은 석순 종유석 순서
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start



input = sys.stdin.readline
n, h = map(int, input().split())
stalagmite, stalactite = [], []
for i in range(n):
    if i % 2 == 0:
        stalagmite.append(int(input()))
    else:
        stalactite.append(int(input()))
stalagmite.sort()
stalactite.sort()

min_value = n
range_cnt = 0
for i in range(1, h+1):
    stalagmite_cnt = len(stalagmite) - binary_search(stalagmite, i - 0.5)
    stalactite_cnt = len(stalactite) - binary_search(stalactite, h - i + 0.5)

    if min_value == stalagmite_cnt + stalactite_cnt:
        range_cnt += 1
    elif min_value > stalagmite_cnt + stalactite_cnt:
        min_value = stalagmite_cnt + stalactite_cnt
        range_cnt = 1
print(min_value, range_cnt)