"""
https://www.acmicpc.net/problem/2589
보물섬
"""
from pprint import pprint


WL = {'W': 0, 'L': 1}
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
MOVES = (UP, DOWN, LEFT, RIGHT)


def in_matrix(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False


def zeros_list(n: int, m: int) -> list:
    """
    :param n: number of row
    :param m: number of column
    :return: zeros list
    """
    row = [0 for _ in range(m)]
    mtx = [row[:] for _ in range(n)]
    # mtx = [deepcopy(row) for _ in range(m)]
    # mtx = [row for _ in range(m)]     모든 row가 같은 주소를 참조하게 되서 mtx[i][j]만 수정해도 mtx[:][j]가 바뀜
    return mtx


def bfs(mtx, start_i, start_j):
    n = len(mtx)
    m = len(mtx[0])
    visit_mtx = zeros_list(n, m)
    max_dist = 0
    queue = [(start_i, start_j, 0)]     # (i, j, node count)
    visit_mtx[start_i][start_j] = 1

    while queue:
        i, j, c = queue.pop(0)
        for di, dj in MOVES:
            new_i = i + di
            new_j = j + dj
            new_c = c + 1
            if in_matrix(new_i, new_j, n, m):
                if visit_mtx[new_i][new_j] == 0:
                    if mtx[new_i][new_j] == 1:
                        visit_mtx[new_i][new_j] = 1             # BFS 큐 넣기 전에 방문 체크 꼭!!
                        queue.append((new_i, new_j, new_c))
                        max_dist = max(max_dist, new_c)

    return max_dist


def main():
    n, m = tuple(map(int, input().rstrip().split(' ')))
    map_ = [list(map(lambda x: WL[x], input().rstrip())) for _ in range(n)]
    # pprint(map_)

    max_dist = 0
    for i in range(n):
        for j in range(m):
            if map_[i][j] == 1:
                max_dist = max(max_dist, bfs(map_, i, j))

    print(max_dist)


if __name__ == '__main__':
    main()
