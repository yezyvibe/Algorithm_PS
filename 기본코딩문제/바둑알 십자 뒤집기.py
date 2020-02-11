go = [list(map(int, input().split())) for i in range(19)]
n = int(input())

for m in range(1,n+1):
    dx, dy = list(map(int, input().split()))
    for k in range(19):
        if go[dx-1][k]!= 0:
            go[dx-1][k]= 0
        else:
            go[dx-1][k]= 1

        if go[k][dy-1]!= 0:
            go[k][dy-1]= 0
        else:
            go[k][dy-1]= 1
for a in go:
    print(' '.join(map(str,a)))