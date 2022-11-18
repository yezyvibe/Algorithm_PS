import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 1
# 100,000 * 10,000 = 1,000,000,000 -> 이분 탐색

start, end = max(arr), n * 10000
while start <= end:
    mid = (start + end) // 2

    cnt = 1
    current_length = 0
    for k in arr:
        if current_length + k <= mid:
            current_length += k
        else: # 블루레이 개수 한개 더 늘리기
            cnt += 1
            current_length = k

    if cnt > m: # m개만 만들어야 하는데 더 많이 만들었다 -> 블루레이 길이 늘리기
        start = mid + 1
    elif cnt <= m: # cnt == m이면 만들어야 하는 개수가 같으니까 -> 블루레이 길이 최대한 줄여보기 -> 왜내면 구하고 싶은건 블루레이의 최소길이이기 때문
        end = mid - 1
        answer = mid

print(answer)