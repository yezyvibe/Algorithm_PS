import sys

input = sys.stdin.readline
g, s = map(int, input().split(' '))
g_lst = [0, g] # 먼저 처음과 끝을 넣어놓고
s_lst = [0, s]
for _ in range(int(input())):
    a, b = map(int, input().rstrip().split(' '))
    if a == 0:
        s_lst.append(b)
    else:
        g_lst.append(b)
g_lst.sort() # 세로점선
s_lst.sort() # 가로점선

max_v = -1
for i in range(1, len(s_lst)):
    for j in range(1, len(g_lst)):
        h = s_lst[i] - s_lst[i-1]
        w = g_lst[j] - g_lst[j-1]
        max_v = max(w*h, max_v)
print(max_v)