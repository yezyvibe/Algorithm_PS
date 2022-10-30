#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minCostPath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. WEIGHTED_INTEGER_GRAPH g
#  2. INTEGER x
#  3. INTEGER y
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
import heapq

def dijkstra(start, end, n, adj):
    hq = [(0, start)]
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    
    while hq:
        cost, node = heapq.heappop(hq)
        if cost > dist[node]:
            continue
        for next_cost, next_node in adj[node]:
            if dist[next_node] > next_cost + cost:
                dist[next_node] = next_cost + cost
                heapq.heappush(hq, (next_cost + cost, next_node))
    return dist[end]
            
def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    # Write your code here
    adj = [[] for _ in range(g_nodes+1)]
    for i in range(len(g_from)):
        adj[g_from[i]].append((g_weight[i], g_to[i]))
        adj[g_to[i]].append((g_weight[i], g_from[i]))
        
    return dijkstra(1, x, g_nodes, adj) + dijkstra(x, y, g_nodes, adj) + dijkstra(y, g_nodes, g_nodes, adj)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    x = int(input().strip())

    y = int(input().strip())

    result = minCostPath(g_nodes, g_from, g_to, g_weight, x, y)

    fptr.write(str(result) + '\n')

    fptr.close()
