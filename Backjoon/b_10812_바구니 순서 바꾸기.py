import sys

input = sys.stdin.readline
n, m = map(int, input().split())
basket = [i for i in range(1,n+1)]
for i in range(m):
    begin, end, mid = map(int, input().split())
    a = basket[:begin-1] + basket[mid-1:end] + basket[begin-1:mid-1] + basket[end:]
    basket = a
print(*basket)