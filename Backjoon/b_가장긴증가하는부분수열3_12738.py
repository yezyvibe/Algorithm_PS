import sys

def binary_search(num):
    start, end = 0, len(lis) - 1
    print(num, lis)
    while start <= end:
        mid = (start + end) // 2

        if lis[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return start


input = sys.stdin.readline
n = int(input())
arr = map(int, input().split())
lis = []

for num in arr:
    if len(lis) == 0:
        lis.append(num)
        continue
    
    if lis[-1] < num:
        lis.append(num)
    else:
        idx = binary_search(num)
        lis[idx] = num
        print("lis:", lis)
print(len(lis))

# import sys
# from bisect import bisect_left


# input = sys.stdin.readline
# n = int(input())
# arr = map(int, input().split())
# lis = []

# for num in arr:
#     if not len(lis):
#         lis.append(num)
#         continue

#     if num > lis[-1]:
#         lis.append(num)
#     else:
#         idx = bisect_left(lis, num)
#         lis[idx] = num

# print(len(lis))



