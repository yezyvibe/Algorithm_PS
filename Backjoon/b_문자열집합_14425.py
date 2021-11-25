import sys

input = sys.stdin.readline
n, m = map(int, input().split())
s_dict = {}
for i in range(n):
    string = input().rstrip()
    s_dict[string] = 1
answer = 0
for j in range(m):
    word = input().rstrip()
    if word in s_dict:
        answer += 1
print(answer)
