t = int(input())

for tc in range(1,t+1):
    p, q, r, s, w = map(int,input().split())
    a = p * w
    if w > r:
        b = q + (w-r)*s
    else:
        b = q
    if a > b:
        res = b
    else:
        res = a
    print(f'#{tc} {res}')