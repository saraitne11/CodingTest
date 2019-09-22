"""
Breadth First Search & Depth First Search
"""
from typing import Dict, Union, Iterable, List
import numpy as np
from pprint import pprint
import random
from copy import deepcopy


alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def zeros_list(n: int, m: int) -> list:
    row = [0 for _ in range(n)]
    mtx = [row[:] for _ in range(m)]
    # mtx = [deepcopy(row) for _ in range(m)]
    # mtx = [row for _ in range(m)]     모든 row가 같은 주소를 참조하게 되서 mtx[i][j]만 수정해도 mtx[i][:]가 바뀜
    return mtx


def check_symmetric(a: np.ndarray, tol=1e-8):
    return np.all(np.abs(a-a.T) < tol)


def graph_list2mtx(adj_list: Dict) -> Union[List, np.ndarray]:
    # make zeros matrix
    num_v = len(adj_list)
    mtx = zeros_list(num_v, num_v)

    for vertex in adj_list:
        # convert to alphabet -> index
        r = alphabet.index(vertex)
        col = list(map(lambda x: alphabet.index(x), sorted(adj_list[vertex])))
        for c in col:
            mtx[r][c] = 1
    return mtx


def graph_mtx2list(adj_mtx: Union[list, np.ndarray]) -> Dict:
    # Get the number of vertex
    num_v = len(adj_mtx)
    # each element = vertex: [adjacent_vertexes]
    adj = {alphabet[i]: [] for i in range(num_v)}
    for vertex in adj:
        # Get row
        row = adj_mtx[alphabet.index(vertex)][:]
        s_idx = 0
        for _ in range(row.count(1)):
            v = row.index(1, s_idx)
            adj[vertex].append(alphabet[v])
            s_idx = v + 1
    return adj


def bfs(graph: Dict, start_node: str) -> List:
    """
    Breadth First Search
    :param graph: adjacent list (Dictionary Type)
    :param start_node: search start vertex
    :return: visit order list
    """
    visit = list()
    queue = list()
    queue.append(start_node)

    while queue:
        # print('queue', q)
        # print('visit', visit)
        # print('==============================')
        node = queue.pop(0)         # 현재 방문 노드
        if node not in visit:       # 현재 노드가 방문한 노드가 아니면
            visit.append(node)
            queue.extend(graph[node])

    return visit


def dfs(graph: Dict, start_node: str) -> List:
    """
    Depth First Search
    :param graph: adjacent list (Dictionary Type)
    :param start_node: search start vertex
    :return: visit order list
    """
    visit = list()
    stack = list()
    stack.append(start_node)

    while stack:
        # print('stack', stack)
        # print('visit', visit)
        # print('==============================')
        node = stack.pop(-1)        # 현재 방문 노드
        if node not in visit:       # 현재 노드가 방문한 노드가 아니면
            visit.append(node)
            # stack.extend(sorted(graph[node], reverse=True))       # For left to right (in picture)
            stack.extend(graph[node])

    return visit


def main():
    adj_list = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    #           A  B  C  D  E  F  G  H  I  J  K  L  M
    adj_mtx = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    # A
               [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],    # B
               [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],    # C
               [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],    # D
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],    # E
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],    # F
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],    # G
               [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],    # H
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],    # I
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],    # J
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],    # K
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],    # L
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]    # M

    # pprint(graph_list2mtx(adj_list))
    # pprint(graph_mtx2list(adj_mtx))

    print(bfs(adj_list, 'A'))
    print(dfs(adj_list, 'A'))


if __name__ == '__main__':
    main()