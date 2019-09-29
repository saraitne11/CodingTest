"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
벽돌깨기
"""
from copy import deepcopy
from pprint import pprint


def is_in_matrix(i, j, n, m):
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


def get_ranges(cur, val, n, m):
    ranges = []
    for r in range(1, val):
        i, j = (cur[0] + r, cur[1])
        if is_in_matrix(i, j, n, m):
            ranges.append((i, j))

        i, j = (cur[0] - r, cur[1])
        if is_in_matrix(i, j, n, m):
            ranges.append((i, j))

        i, j = (cur[0], cur[1] + r)
        if is_in_matrix(i, j, n, m):
            ranges.append((i, j))

        i, j = (cur[0], cur[1] - r)
        if is_in_matrix(i, j, n, m):
            ranges.append((i, j))
    return ranges


def drop(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for j in range(m):
        col = list(map(lambda row: row[j], matrix))
        non_zeros = []
        for c in col:
            if c != 0:
                non_zeros.append(c)

        for i in range(n-1, -1, -1):
            if non_zeros:
                matrix[i][j] = non_zeros.pop()
            else:
                matrix[i][j] = 0


def eliminations(matrix, start):
    n = len(matrix)         # h
    m = len(matrix[0])      # w

    def eliminate(cur):
        val = matrix[cur[0]][cur[1]]
        matrix[cur[0]][cur[1]] = 0
        chains = get_ranges(cur, val, n, m)

        for c in chains:
            eliminate(c)

    eliminate(start)
    return


def get_surface(matrix):
    n = len(matrix)         # h
    m = len(matrix[0])      # w
    surfaces = [(-1, j) for j in range(m)]

    for j in range(m):
        for i in range(n):
            if matrix[i][j] != 0:
                surfaces[j] = (i, j)
                break

    return surfaces


def count_bricks(matrix):
    n = len(matrix)         # h
    m = len(matrix[0])      # w
    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                cnt += 1
    return cnt


def search(matrix, num_shot):

    remainders = []

    def simulation(mtx, pos, n):
        """
        :param mtx: matrix
        :param pos: shot position (i, j)
        :param n: number of remain shot
        """
        mtx = deepcopy(mtx)         # Do not touch original
        eliminations(mtx, pos)      # Eliminations
        drop(mtx)                   # Drop
        n -= 1
        r = count_bricks(mtx)       # number of current bricks
        if r == 0 or n == 0:
            remainders.append(r)
            return r
        else:
            for s in get_surface(mtx):
                if s[0] != -1:
                    simulation(mtx, s, n)

    for surface in get_surface(matrix):
        if surface[0] != -1:
            n_remain = simulation(matrix, surface, num_shot)
            if n_remain == 0:
                return 0

    return min(remainders)


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        n, w, h = list(map(int, input().rstrip().split(' ')))

        brick_matrix = [list(map(int, input().rstrip().split(' '))) for _ in range(h)]

        # print(n, w, h)

        # print('==========================================')
        # pprint(brick_matrix)
        # print(get_surface(brick_matrix))
        # print('==========================================')
        #
        # eliminations(brick_matrix, (1, 2))
        # drop(brick_matrix)
        # print('==========================================')
        # pprint(brick_matrix)
        # print(get_surface(brick_matrix))
        # print('==========================================')

        # print(search(brick_matrix, 2))

        # eliminations(brick_matrix, (2, 2))
        # drop(brick_matrix)
        # print(get_surface(brick_matrix))
        # print('==========================================')
        # pprint(brick_matrix)
        # print(get_surface(brick_matrix))
        # print('==========================================')

        print('#%d %d' % (t+1, search(brick_matrix, n)))
        # break


if __name__ == '__main__':
    main()