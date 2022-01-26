import sys 
from itertools import combinations

n = int(input())
nums = []
for i in range(1, 11):
    for combi in combinations(range(0, 10), i):
        combi = sorted(list(combi), reverse=True)
        nums.append(int("".join(map(str, combi))))
nums.sort()

try:
    print(nums[n])
except:
    print(-1)