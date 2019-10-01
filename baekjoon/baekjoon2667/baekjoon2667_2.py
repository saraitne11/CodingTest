"""
https://www.acmicpc.net/problem/2667
"""

from pprint import pprint

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def zeros_list(n: int, m: int) -> list:
    """
    :param n: number of row
    :param m: number of column
    :return: zeros list
    """
    row = [0 for _ in range(m)]
    mtx = [row[:] for _ in range(n)]
    # mtx = [deepcopy(row) for _ in range(m)]
    # mtx = [row for _ in range(m)]     모든 row가 같은 주소를 참조하게 되서 mtx[i][j]만 수정해도 mtx[i][:]가 바뀜
    return mtx


def in_matrix(i, j, n, m):
    """
    :param i: i(row) coordinate
    :param j: j(column) coordinate
    :param n: length of row
    :param m: length of column
    :return: True or False
    """
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False


def dfs1(mtx, start_i, start_j):
    n = len(mtx)
    visited = []

    cnt = [0]

    def search(i, j):
        cnt[0] += 1
        mtx[i][j] = 0
        visited.append((i, j))
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if in_matrix(ni, nj, n, n):
                if mtx[ni][nj] == 1:
                    search(ni, nj)

    search(start_i, start_j)
    # print(cnt[0])
    return len(visited)


def dfs2(mtx, start_i, start_j):
    n = len(mtx)
    visited = []

    cnt = [0]

    def search(i, j):
        cnt[0] += 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if in_matrix(ni, nj, n, n):
                if mtx[ni][nj] == 1:
                    mtx[ni][nj] = 0       # 서치 하기 전에 방문 처리
                    visited.append((start_i, start_j))
                    search(ni, nj)

    mtx[start_i][start_j] = 0           # 서치 하기 전에 방문 처리
    visited.append((start_i, start_j))
    search(start_i, start_j)
    # print(cnt[0])
    return len(visited)


def divisions_print(n, divisions):
    mtx = zeros_list(n, n)
    ds = sorted(divisions, key=len)
    for i, d in enumerate(ds):
        for x, y in d:
            mtx[x][y] = i+1
    pprint(mtx)
    return


def main():
    n = int(input().rstrip())
    mtx = [list(map(int, input().rstrip())) for _ in range(n)]
    # print(n)
    # pprint(mtx)

    divis = []
    for i in range(n):
        for j in range(n):
            if mtx[i][j] == 1:
                divis.append(dfs2(mtx, i, j))

    print(len(divis))
    divis.sort()
    for d in divis:
        print(d)


if __name__ == '__main__':
    main()
