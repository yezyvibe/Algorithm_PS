import heapq

def solution(n, paths, gates, summits):
    # 인접 배열 만들기
    INF = float('inf')
    dist = [INF] * (n+1)
    summits_set = set(summits)
    answer = [0, INF]
    summits.sort()
    hq = []

    adj = [[] for _ in range(n+1)]
    for path in paths:
        i, j, w = path
        adj[i].append((w, j))
        adj[j].append((w, i))

    # 각 봉우리에서 다익스트라 알고리즘 탐색
    for gate in gates:
        heapq.heappush(hq, (0, gate))
        dist[gate] = 0

    while hq:
        intensity, node = heapq.heappop(hq)
        if intensity > dist[node] or node in summits_set:
            continue
        for next_intensity, next_node in adj[node]:
            # 현재 인텐서티 보다 크고, 지나간 것들 중에 인텐서티 작으면 업데이트
            if intensity <= next_intensity and dist[next_node] > next_intensity:
                dist[next_node] = next_intensity
                heapq.heappush(hq, (next_intensity, next_node))
            elif intensity > next_intensity and dist[next_node] > intensity:
                dist[next_node] = intensity
                heapq.heappush(hq, (intensity, next_node))
    # 후보가 되는 등산 코스가 여러 개라면 산봉우리 번호 가장 작은 것이 정답
    for summit in summits:
        if dist[summit] < answer[1]:
            answer[0] = summit
            answer[1] = dist[summit]

    return answer


n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3, 7]
summits = [1, 5]
print(solution(n, paths, gates, summits))