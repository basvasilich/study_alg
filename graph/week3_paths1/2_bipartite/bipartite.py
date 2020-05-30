# Uses python3

import sys
from collections import deque


def bipartite(adj):
    colors = {}

    def helper(node):
        q = deque()
        q.append((node, 'r'))
        while len(q):
            node, color = q.popleft()
            adj_node = adj[node]
            if node in colors and color != colors[node]:
                return False

            colors[node] = color

            if len(adj_node) > 0:
                for node in adj_node:
                    if node not in colors:
                        q.append((node, 'b' if color == 'r' else 'r'))
                    elif color == colors[node]:
                        return False
        return True

    return 1 if all(helper(node) for node in range(len(adj)) if node not in colors) else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
