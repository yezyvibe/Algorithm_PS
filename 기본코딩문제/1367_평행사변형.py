# n = int(input())
#
# for i in range(1,n+1):
#     print(' '*(n-i) + '*'*n)

h, k, d = map(str, input().split())
h = int(h)
k = int(k)

if d == 'L':
    for j in range(k, -1, -1):
        print(' '*(k-j) + '*'*k)
elif d == 'R':
    for i in range(0,k+1):
        print(' '*(k-i) + '*'*k)
