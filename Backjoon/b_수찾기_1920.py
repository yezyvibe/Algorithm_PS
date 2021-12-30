import sys

def binary_search(target, n_list):
    start = 0
    end = len(n_list)

    while start <= end:
        mid = (start + end) // 2
        if mid >= len(n_list):
            return False
        if n_list[mid] == target:
            return True
        elif n_list[mid] > target:
            end = mid - 1
        elif n_list[mid] < target:
            start = mid + 1
    return False


input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
n_list.sort()

for i in range(m):
    target = numbers[i]
    if binary_search(target, n_list):
        print(1)
    else:
        print(0)