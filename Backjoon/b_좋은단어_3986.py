import sys


input = sys.stdin.readline
answer = 0
for i in range(int(input())):
    stack = []
    word = input().rstrip()
    if len(word) % 2 == 0:
        for j in word:
            if not stack:
                stack.append(j)
            else:
                if j == stack[-1]:
                    stack.pop()
                else:
                    stack.append(j)
        if not stack:
            answer += 1
print(answer)

