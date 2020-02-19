n, m, i = map(int, input().split())

for j in range(n):
    for k in range(m):
        for l in range(i):
            print(j, k, l, sep= ' ')
print(n*m*i)