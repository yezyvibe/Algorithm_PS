import sys
sys.setrecursionlimit(1000000)
n = int(input())

def sum(n, sum2):
    if n == 0:
        print(sum2)
    else:
        sum2 += n
        sum(n-1, sum2)

sum2 = 0
sum(n,sum2)