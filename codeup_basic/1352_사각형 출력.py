# n = int(input())
# arr = [['*']*n for i in range(n)]
#
# for a in arr:
#     print(''.join(map(str,a)))


# 다른 풀이
n = int(input())
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()