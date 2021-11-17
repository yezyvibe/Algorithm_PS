import sys

input = sys.stdin.readline
n = int(input())
positive = []
negative = []
answer = 0
for i in range(n):
    number = int(input())
    if number > 1:
        positive.append(number)
    elif number == 1:
        answer += 1
    else:
        negative.append(number)

positive.sort(reverse=True)
negative.sort()

# 양수 더하기
if len(positive) % 2 == 0:
    for i in range(1, len(positive), 2):
        answer += (positive[i] * positive[i-1])
else:
    for i in range(1, len(positive)-1, 2):
        answer += (positive[i] * positive[i-1])
    answer += positive[len(positive)-1]
# 음수 더하기

if len(negative) % 2 == 0:
    for i in range(1, len(negative), 2):
        answer += (negative[i] * negative[i-1])
else:
    for i in range(1, len(negative)-1, 2):
        answer += (negative[i] * negative[i-1])
    answer += negative[len(negative)-1]

print(answer)