import sys

a, b = sys.stdin.readline().split()
cnt = 0
gap = 0
min_value = 50

for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(i, i+len(a)):
        idx = j-i
        if a[idx] == b[j]:
            cnt += 1
    gap = len(a) - cnt
    if min_value > gap:
        min_value = gap

print(min_value)
sys.exit()