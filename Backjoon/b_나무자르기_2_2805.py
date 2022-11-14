import sys


input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

start, end = 0, trees[-1] # 절단기 높이가 기준
answer = 0
while start <= end:
    mid = (start + end) // 2

    total = 0
    for tree in trees:
        if mid < tree:
            total += (tree - mid)
    if total >= m:
        # 내가 필요한 것보다 더 많아 -> 절단기 높이 올리기
        start = mid + 1
        answer = mid
    else:
        # 내가 필요한 것보다 적어 -> 절단기 높이 내리기
        end = mid - 1
print(answer)