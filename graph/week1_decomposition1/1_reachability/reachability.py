# Uses python3

import sys


def reach(adj, x, y):
    visited = set()
    flag = 0

    if not len(adj):
        return 0

    def explore(v, f):
        visited.add(v)
        if v == y:
            return 1

        if len(adj[v]):
            for i in adj[v]:
                if i not in visited:
                    f = explore(i, f)
                    if f:
                        break

        return f

    if x == y:
        return 1

    return explore(x, flag)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
