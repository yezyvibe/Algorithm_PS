from sys import stdin

input = stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
cnt, s, res = 1, [], [] # res 결과값 리스트

for i in nums:
    while i >= cnt:
        s.append(cnt)
        res.append('+')
        cnt += 1
    if s.pop() != i:
        print('NO')
        break
    else:
        res.append('-')
else:
    print('\n'.join(res))


