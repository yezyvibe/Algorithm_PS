import sys

def calcultate(num, idx, p, m, g, d):
    global min_v, max_v
    
    if idx == n:
        max_v = max(max_v, num)
        min_v = min(min_v, num)
        return

    if p:
        calcultate(num+numbers[idx], idx+1, p-1, m, g, d)
    if m:
        calcultate(num-numbers[idx], idx+1, p, m-1, g, d)
    if g:
        calcultate(num*numbers[idx], idx+1, p, m, g-1, d)
    if d:
        calcultate(int(num/numbers[idx]), idx+1, p, m, g, d-1)

input = sys.stdin.readline
n = int(input())
min_v, max_v = sys.maxsize, -sys.maxsize-1
numbers = list(map(int ,input().rstrip().split()))
p, m, g, d = map(int, input().split(' '))
calcultate(numbers[0], 1, p, m, g, d)
print(max_v)
print(min_v)