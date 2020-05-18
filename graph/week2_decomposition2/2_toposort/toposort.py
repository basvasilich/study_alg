# Uses python3

import sys


def dfs(adj, used, order, x):
    for n in adj[x]:
        if used[n] == 0:
            order, used = dfs(adj, used, order, n)

    if used[x] == 0:
        used[x] = 1
        order.append(x)
    return order, used


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for v in range(len(adj)):
        if used[v] == 0:
            order, used = dfs(adj, used, order, v)
    return list(reversed(order))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
