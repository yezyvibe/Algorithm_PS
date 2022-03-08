import sys

input = sys.stdin.readline
t_e, t_s, t_m = map(int, input().split())
e, s, m = 1, 1, 1
answer = 1
while True:
    if e == t_e and s == t_s and m == t_m:
        print(answer)
        break
    answer += 1
    e += 1
    s += 1
    m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
