"""
https://www.acmicpc.net/problem/2667
"""

from pprint import pprint

# 상(0, -1) 하(0, 1) 좌(-1, 0) 우(1, 0)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


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


def is_in_matrix(x, y, n, m):
    """
    :param x: x(row) coordinate
    :param y: y(column) coordinate
    :param n: length of row
    :param m: length of column
    :return: True or False
    """
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


def search(mtx, x, y):
    """
    :param mtx: input matrix
    :param x: current coordinate of row
    :param y: current coordinate of column
    :return: indices of apartments division
    """
    n = len(mtx)    # n by n 행렬
    # 현재 노드 방문하고 삭제
    mtx[x][y] = 0
    visit = [(x, y)]
    q = [(x, y)]
    while q:
        x, y = q.pop(0)
        for k in range(4):      # 상하좌우 탐색
            nx = x + dx[k]
            ny = y + dy[k]
            if is_in_matrix(nx, ny, n, n):
                if mtx[nx][ny] == 1:
                    mtx[nx][ny] = 0             # 방문 노드 삭제
                    visit.append((nx, ny))      # 현재 단지에 추가
                    q.append((nx, ny))
    return visit


def search_recursive(mtx, start_x, start_y):
    n = len(mtx)    # n by n 행렬
    visit = []

    def chain(x, y):
        # 현재 노드 방문하고 삭제
        mtx[x][y] = 0
        visit.append((x, y))
        for k in range(4):      # 상하좌우 탐색
            nx = x + dx[k]
            ny = y + dy[k]
            if is_in_matrix(nx, ny, n, n):
                if mtx[nx][ny] == 1:
                    chain(nx, ny)

    chain(start_x, start_y)
    return visit


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

    divisions = []
    for i in range(n):
        for j in range(n):
            if mtx[i][j] == 1:
                # v = search(mtx, i, j)
                v = search_recursive(mtx, i, j)
                divisions.append(v)
                # print(v)
                # pprint(mtx)

    divisions.sort(key=len)
    # divisions.sort(key=lambda x: len(x))
    # divisions_print(n, divisions)
    print(len(divisions))
    for a in divisions:
        print(len(a))


if __name__ == '__main__':
    main()
