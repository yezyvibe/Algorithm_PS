import sys

input = sys.stdin.readline
n, m = map(int, input().split())
s_dict = {}
for i in range(n):
    string = input().rstrip()
    if string[0] in s_dict:
        s_dict[string[0]].append(string)
    else:
        s_dict[string[0]] = [string]
answer = 0
for i in range(m):
    word = input().rstrip()
    if word[0] in s_dict:
        for j in s_dict[word[0]]:
            if word == j[:len(word)]:
                answer += 1
                break
print(answer)
