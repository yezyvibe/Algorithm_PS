import sys

input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
answer = 0
for num in n_list:
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        answer += 1
print(answer)