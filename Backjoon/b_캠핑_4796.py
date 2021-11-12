import sys

input = sys.stdin.readline
idx = 1
while True:
    l, p, v = map(int, input().rstrip().split())
    if l == p == v == 0:
        break
    if v % p <= l:
        q, r = divmod(v, p)
        print(f"Case {idx}: {(q*l)+r}")
    else:
        q, r = divmod(v, p)
        print(f"Case {idx}: {(q*l)+l}")
    idx += 1