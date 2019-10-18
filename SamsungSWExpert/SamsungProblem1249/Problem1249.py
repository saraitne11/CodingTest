"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE
1249. [S/W 문제해결 응용] 4일차 - 보급로
"""
from collections import deque


MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def const_matrix(value, n, m):
    row = [value for _ in range(m)]
    mtx = [row[:] for _ in range(n)]
    return mtx


def in_matrix(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False


def bfs(_map, n):
    cum_val = const_matrix(99999, n, n)
    queue = deque([(0, 0)])
    cum_val[0][0] = _map[0][0]

    while queue:
        cur = queue.popleft()
        ci, cj = cur[0], cur[1]
        for di, dj in MOVES:
            ni = ci + di
            nj = cj + dj
            if in_matrix(ni, nj, n, n):
                v = cum_val[ci][cj] + _map[ni][nj]
                if cum_val[ni][nj] > v:
                    cum_val[ni][nj] = v
                    queue.append((ni, nj))

    # from pprint import pprint
    # pprint(cum_val)
    return cum_val[n-1][n-1]


def main():
    test_cases = int(input())
    for t in range(test_cases):
        n = int(input())
        _map = [list(map(int, list(input().rstrip()))) for _ in range(n)]
        print('#%d %d' % (t+1, bfs(_map, n)))


if __name__ == '__main__':
    main()
