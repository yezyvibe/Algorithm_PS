import sys, heapq

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]  # 연결된 간선
check = [0 for _ in range(n + 1)]  # 노드의 진입차수
heap = []  # 최소힙으로 낮은 숫자의 문제를 먼저 뽑는 것
result = []  # 결과값

for i in range(int(m)):
    a, b = map(int, input().split())
    arr[a].append(b)  # 노드 간 연결 관계 나타내기
    check[b] += 1  # 해당 노드 진입차수 +1

for i in range(1, n + 1):
    if check[i] == 0:
        heapq.heappush(heap, i)

while heap:
    num = heapq.heappop(heap)
    result.append(num)
    for i in arr[num]:
        check[i] -= 1
        if check[i] == 0:
            heapq.heappush(heap, i)
print(*result)
