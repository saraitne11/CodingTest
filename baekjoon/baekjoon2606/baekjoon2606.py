"""
https://www.acmicpc.net/problem/2606
"""
from collections import deque


def dfs(graph, start=1):
    visited = []

    def search(current):
        for adj in graph[current]:
            if adj not in visited:
                visited.append(adj)
                search(adj)

    visited.append(start)
    search(start)
    # print(visited)
    return len(visited) - 1


def bfs(graph, start=1):
    queue = deque([start])
    visited = []

    while queue:
        cur = queue.popleft()
        if cur not in visited:
            visited.append(cur)
            queue.extend(graph[cur])

    # print(visited)
    return len(visited) - 1


def main():
    n_nodes = int(input().rstrip())
    n_edges = int(input().rstrip())
    graph = {(i+1): [] for i in range(n_nodes)}

    for _ in range(n_edges):
        a, b = tuple(map(int, input().rstrip().split(' ')))
        graph[a].append(b)
        graph[b].append(a)

    # print(graph)
    print(dfs(graph, 1))
    # print(bfs(graph, 1))
    return


if __name__ == '__main__':
    main()
