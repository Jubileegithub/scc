from mpi4py import MPI
import sys

def read_graph(filename):
    with open(filename, "r") as f:
        n, m = map(int, f.readline().split())
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            adj[u].append(v)
            adj[v].append(u)
    return adj

def bfs_mpi(adj, start, comm):
    rank = comm.Get_rank()
    size = comm.Get_size()
    n = len(adj)

    dist = [-1] * n
    if rank == 0:
        frontier = [start]
        dist[start] = 0
    else:
        frontier = []

    frontier = comm.bcast(frontier, root=0)
    dist = comm.bcast(dist, root=0)

    level = 0

    while True:
        local_frontier = frontier[rank::size]
        local_next = []

        for v in local_frontier:
            for u in adj[v]:
                if dist[u] == -1:
                    dist[u] = level + 1
                    local_next.append(u)

        all_next = comm.allgather(local_next)
        frontier = list(set(v for part in all_next for v in part))

        dist = comm.allreduce(dist, op=MPI.MAX)

        if not frontier:
            break

        level += 1

    return dist

if __name__ == "__main__":
    graph = sys.argv[1]
    start = int(sys.argv[2])

    comm = MPI.COMM_WORLD
    adj = read_graph(graph)

    dist = bfs_mpi(adj, start, comm)

    if comm.Get_rank() == 0:
        for i, d in enumerate(dist):
            print(i, d)
