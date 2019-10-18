"""
파이썬 SW문제해결 응용_구현 - 02 완전 검색
5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
"""

MOVES = [(1, 0), (0, 1)]


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


def dfs(mtx, start, end):
    """
    :param mtx: matrix
    :param start: (i, j)
    :param end: (i, j)
    :return: minimum value
    """
    n = len(mtx)
    m = len(mtx[0])
    # val_ = []
    min_val = [999999]

    def search(current, cum_val):
        if current == end:
            if min_val[0] > cum_val:
                # 마지막 노드에서 현재 가지고 있는 최소값보다
                # 현재까지 누적이 더 작으면 최소값 교체
                min_val[0] = cum_val
            return
        else:
            for di, dj in MOVES:
                ni = current[0] + di
                nj = current[1] + dj
                next_ = (ni, nj)
                if in_matrix(ni, nj, n, m):
                    if min_val[0] >= cum_val:
                        # DFS 중 현재까지 누적합이 이미 지금 가지고 있는 최소값보다 크면
                        # 지금 경로는 최소값이 될 수 없으므로 탐색 중지
                        new_val = cum_val + mtx[ni][nj]
                        search(next_, new_val)

    start_value = mtx[start[0]][start[1]]
    search(start, start_value)
    return min_val[0]


def main():
    test_cases = int(input())
    for t in range(test_cases):
        n = int(input())
        mtx = [list(map(int, input().split(' '))) for _ in range(n)]

        # from pprint import pprint
        # pprint(mtx)
        # print(dfs(mtx, (0, 0), (n-1, n-1)))
        ans = dfs(mtx, (0, 0), (n-1, n-1))
        print('#%d %d' % (t+1, ans))

    # import random
    # n = 13
    # mtx = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
    # ans = dfs(mtx, (0, 0), (n - 1, n - 1))
    # print('#%d %d' % (5 + 1, ans))


if __name__ == '__main__':
    main()
