t = int(input())
for tc in range(1,t+1):
    n = input()
    m = input()
    for i in range(len(m)-len(n)+1):
        if m[i:i+len(n)] == n:
            result = 1
            break
        else:
            result = 0
    print('#{} {}'.format(tc, result))