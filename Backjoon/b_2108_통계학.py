import sys
from collections import Counter

input = sys.stdin.readline
numbers = []
n = int(input())
arithmetic_mean = 0
for i in range(n):
    num = int(input())
    arithmetic_mean += num
    numbers.append(num)

numbers.sort()
median = numbers[n//2]
range_ = numbers[-1] - numbers[0]

mode_list = Counter(numbers).most_common()
if len(mode_list) > 1 and mode_list[0][1] == mode_list[1][1]:
    mode = mode_list[1][0]
else:
    mode = mode_list[0][0]

print(round(arithmetic_mean/n))
print(median)
print(mode)
print(range_)