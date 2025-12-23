import random
import sys

def generate_graph(n, m, filename):
    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))

    with open(filename, "w") as f:
        f.write(f"{n} {len(edges)}\n")
        for u, v in edges:
            f.write(f"{u} {v}\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_graph.py N M graph.txt")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])
    filename = sys.argv[3]

    generate_graph(n, m, filename)
