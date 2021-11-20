import sys

input = sys.stdin.readline
s = input().rstrip()
s = s.upper()
s_dict = {}
for i in s:
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] += 1
max_v = 0
answer = ''
for key, val in s_dict.items():
    if val > max_v:
        answer = key
        max_v = val
    elif val == max_v:
        answer = '?'
print(answer)