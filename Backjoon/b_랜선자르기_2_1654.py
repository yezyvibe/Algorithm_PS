import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [ int(input()) for _ in range(k)]
arr.sort()

# 자르는 랜선의 길이가 기준값
# 종료 조건은 필요한 랜선 개수 n개를 만들 수 있는지

start, end = 1, arr[-1]
answer = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(len(arr)):
        cur_line = arr[i]
        if cur_line >= mid:
            cnt += (cur_line // mid)

    if cnt >= n: # 목표한 n개 이상 만든다면 -> 랜선 길이 늘리기
        start = mid + 1
        answer = mid
    else: # n개를 못 만드는 경우 -> 길이 줄이기
        end = mid - 1

print(answer)
    
