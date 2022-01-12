import sys

def binary_search(item_a, life_b):
    start, end = 0, len(life_b) - 1
    while start <= end:
        mid = (start + end) // 2
        if item_a > life_b[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    life_a = list(map(int, input().split()))
    life_b = list(map(int, input().split()))
    life_a.sort()
    life_b.sort()
    answer = 0
    for item in life_a:
        answer += binary_search(item, life_b)
    print(answer)

