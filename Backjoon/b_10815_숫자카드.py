import sys

input = sys.stdin.readline
n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

n_dict = {}
for i in n_list:
    if i not in n_dict:
        n_dict[i] = 1
    else:
        n_dict[i] += 1
answer = []
for i in m_list:
    if i in n_dict:
        answer.append(n_dict[i])
    else:
        answer.append(0)
print(*answer)