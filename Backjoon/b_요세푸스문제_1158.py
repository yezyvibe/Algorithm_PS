from collections import deque

n, k = map(int, input().split())
q = deque([ i for i in range(1, n +1)])
cnt = 0
answer = []
while q:
    front = q.popleft()
    cnt += 1
    if cnt == k:
        answer.append(front)
        cnt = 0
    else:
        q.append(front)
answer = "<"+ ", ".join(map(str, answer)) + ">"
print(answer)