T = int(input())

for t in range(1, T+1):
    m1, d1, m2, d2 = map(int,input().split())
    calen =[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = 0
    for i in range(m1, m2):
        d += calen[i]
    d = d + d2 + 1 - d1
    print(f'#{t} {d}')