# Uses python3

import sys


def acyclic(adj):
    visited = set()
    cyclic = set()

    def dfs(v, visited, cyclic):
        visited.add(v)
        cyclic.add(v)

        for n in adj[v]:
            if n not in visited:
                if dfs(n, visited, cyclic):
                    return 1
            elif n in cyclic:
                return 1

        cyclic.remove(v)

        return 0

    for v in range(len(adj)):
        if v not in visited:
            if dfs(v, visited, cyclic):
                return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
