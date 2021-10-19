n = int(input())
peak = list(map(int, input().split()))
answer = 0
cnt = 0
max_peak = 0
for i in peak:
    if i > max_peak:
        max_peak = i
        cnt = 0
    else:
        cnt += 1
    answer = max(answer, cnt)
print(answer)