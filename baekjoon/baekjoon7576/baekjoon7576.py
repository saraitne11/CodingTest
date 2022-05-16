"""
https://www.acmicpc.net/problem/7576
토마토
"""
from pprint import pprint
from collections import deque


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


def bfs(mtx, starts):
    """
    :param mtx: matrix
    :param starts: [(i1, j1), (i2, j2), ...]
    :return:
    """
    n = len(mtx)
    m = len(mtx[0])

    queue = deque()
    for i, j in starts:
        queue.append((i, j, 0))

    max_d = 0
    while queue:
        # list.pop(0) 는 추가적으로 O(N)을 소모함. 앞으로 한칸씩 다 땡켜줘야해서
        i, j, d = queue.popleft()
        for di, dj in MOVES:
            new_i = i + di
            new_j = j + dj
            new_d = d + 1

            if in_matrix(new_i, new_j, n, m):
                if mtx[new_i][new_j] == 0:
                    mtx[new_i][new_j] = 1
                    queue.append((new_i, new_j, new_d))
                    max_d = max(max_d, new_d)
    return max_d


def main():
    m, n = tuple(map(int, input().rstrip().split(' ')))
    # print(n, m)
    map_ = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
    # pprint(map_)

    starts = []
    for i in range(n):
        for j in range(m):
            if map_[i][j] == 1:
                starts.append((i, j))

    max_day = bfs(map_, starts)

    for i in range(n):
        for j in range(m):
            if map_[i][j] == 0:
                print(-1)
                return

    print(max_day)
    return


if __name__ == '__main__':
    main()
