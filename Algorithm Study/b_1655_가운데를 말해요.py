import sys
import heapq

# min heap, max heap 모두 사용

input = sys.stdin.readline
left, right = [], []  # left:큰값->작은값,right:작은값->큰값 순서
for _ in range(int(input())):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -num)  # max heap
    else:
        heapq.heappush(right, num)  # min heap

    if right and -left[0] > right[0]:  # left값이 right값보다 작은지 체크
        left_v = -heapq.heappop(left)
        right_v = heapq.heappop(right)
        heapq.heappush(left, -right_v)
        heapq.heappush(right, left_v)

    print(-left[0])  # 중간값 출력
