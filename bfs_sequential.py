import sys
from collections import deque

def read_graph(filename):
    with open(filename, "r") as f:
        n, m = map(int, f.readline().split())
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            adj[u].append(v)
            adj[v].append(u)
    return adj

def bfs(adj, start):
    n = len(adj)
    dist = [-1] * n
    q = deque([start])
    dist[start] = 0

    while q:
        v = q.popleft()
        for u in adj[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)
    return dist

if __name__ == "__main__":
    graph = sys.argv[1]
    start = int(sys.argv[2])

    adj = read_graph(graph)
    dist = bfs(adj, start)

    for i, d in enumerate(dist):
        print(i, d)
