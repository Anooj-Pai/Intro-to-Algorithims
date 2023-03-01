from heapdict import heapdict
from typing import List, Tuple


def dijkstra(G: List[Tuple[int, int, int]], s: int) -> Tuple[List[int], List[List[int]]]:
    n = max(max(u, v) for u, v, _ in G)  # number of vertices
    dist = [float('inf')] * (n + 1)  # distance from s to each vertex
    prev = [None] * (n + 1)  # previous vertex on shortest path

    dist[s] = 0

    H = heapdict()
    for u in range(1, n + 1):
        H[u] = dist[u]

    # Dijkstra's algorithm
    while H:
        u, d = H.popitem()  # delete vertex with smallest dist[u]
        for uu, v, w in G:
            if uu == u:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    H[v] = dist[v]  # decrease key of v in H

    # construct shortest paths
    paths = [[] for _ in range(1, n + 1)]
    for v in range(1, n + 1):
        if prev[v] is not None:
            path = [v]
            while path[-1] != s:
                path.append(prev[path[-1]])
            path.reverse()
            paths[v-1] = path

    return dist, paths


f = open("rome99.txt", "r")
G = []
for line in f:
    u, v, w = map(int, line.split())
    G.append((u, v, w))

dist, paths = dijkstra(G, 1)

# print output
for v in range(1, len(dist)):
    print(f"{v}:{dist[v]}, {paths[v-1]}")
