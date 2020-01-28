def mtx2list(adj_mtx):
    num_v = len(adj_mtx)
    adj = {i: [] for i in range(num_v)}
    for vertex in adj:
        row = adj_mtx[vertex][:]
        for i, v in enumerate(row):
            if v == 1 and i != vertex:
                adj[vertex].append(i)
    return adj


def dfs(graph, start_node):
    visit = []
    stack = []
    stack.append(start_node)

    while stack:
        node = stack.pop(-1)
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


def solution(n, computers):
    adj_list = mtx2list(computers)
    keys = list(adj_list.keys())

    nets = []

    while adj_list:
        visit = dfs(adj_list, keys[0])
        for v in visit:
            adj_list.pop(v)
            keys.remove(v)
        nets.append(visit)

        # print(visit)
        # print(adj_list)
        # print(keys)

    return len(nets)


if __name__ == '__main__':
    ans = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(ans)
