from sys import stdin


def check(a, b, c, prev):

    if [a, b, c] == cnt:
        print(''.join(answer))
        exit(0)

    if dp[a][b][c][prev[0]][prev[1]]:
        return False

    dp[a][b][c][prev[0]][prev[1]] = True

    if a + 1 <= cnt[A]:
        answer[a + b + c] = 'A'
        if check(a + 1, b, c, [prev[1], A]):
            return True

    if b + 1 <= cnt[B]:
        answer[a + b + c] = 'B'
        if prev[1] != B:
            if check(a, b + 1, c, [prev[1], B]):
                return True

    if c + 1 <= cnt[C]:
        answer[a + b + c] = 'C'
        if prev[0] != C and prev[1] != C:
            if check(a, b, c + 1, [prev[1], C]):
                return True
    return False


A, B, C = 0, 1, 2
s = list(stdin.readline().rstrip())
n = len(s)
answer = [''] * n
cnt = [s.count(word) for word in ('A', 'B', 'C')]
dp = [[[[[0 for _ in range(3)] for _ in range(3)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
check(0, 0, 0, [0, 0])
print(-1)
