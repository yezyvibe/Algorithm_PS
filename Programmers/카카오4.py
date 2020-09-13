import heapq
def solution(n, s, a, b, fares):
    answer = 0
    # 인접리스트
    adj = {i+1: [] for i in range(n)}
    for i in range(len(fares)):
        st, e, c = fares[i]
        adj[st].append([e, c])
        adj[e].append([st, c])
    # for key, value in adj.items():
    #     print(key, value)
    k_list = [0]*(n+1)
    # print(s,a,b)
    asdf = []
    for start in [s,a,b]:
        mst = [False] * (n+1)
        pq = []
        kk = [float('inf')] * (n+1)
        kk[start] = 0
        heapq.heappush(pq, (0, start))
        result = 0
        while pq:
            k, u = heapq.heappop(pq)
            if mst[u]:
                continue
            mst[u] = True
            result += k
            for dest, w in adj[u]:
                if not mst[dest]:
                    kk[dest] = min(k + w, kk[dest])
                    heapq.heappush(pq, (kk[dest], dest))
                    # print(f'내위치: {u}, 현재가중치: {k}')
                    # print(kk)
                    # print()
        # print(result)
        # print('끝')
        asdf.append(kk)
    # print('뭐')
    answer = [0]*(n+1)
    # print(answer)
    # print(asdf)
    for i in range(len(asdf)):
        for j in range(len(asdf[i])):
            answer[j] += asdf[i][j]
    # print(min(answer))
    return min(answer)