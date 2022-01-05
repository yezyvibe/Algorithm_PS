# from bisect import bisect_left


# bisect 라이브러리 사용
# n = int(input())
# arr = list(map(int, input().split()))
# lis = [0]

# for number in arr:
#     if number > lis[-1]:
#         lis.append(number)
#     else:
#         index = bisect_left(lis, number)
#         lis[index] = number
# print(len(lis)-1)


import sys

def binary_search(num):
    start, end = 0, len(lis) - 1
    while start <= end:
        middle = (start + end) // 2
        if lis[middle] >= num:
            end = middle - 1
        elif lis[middle] < num:
            start = middle + 1
    return start

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
lis = [0]

for number in arr:
    if number > lis[-1]:
        lis.append(number)
    else:
        index = binary_search(number)
        lis[index] = number
print(len(lis) - 1)