"""
미생물 격리
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl
"""

from typing import List

DIRECTION = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}


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


class Germ(object):
    def __init__(self, row, col, direction, num):
        self.row = row
        self.col = col
        self.d = direction
        self.num = num

    @property
    def loc(self):
        return self.row, self.col

    def move(self, map_size):
        self.row += self.d[0]
        self.col += self.d[1]
        if self.is_edge(map_size):
            self.edge_op()

    def is_edge(self, n):
        if self.row == 0 or self.row == n-1 or self.col == 0 or self.col == n-1:
            return True
        else:
            return False

    def edge_op(self):
        self.num = self.num // 2
        self.d = (-(self.d[0]), -(self.d[1]))


def crash_op(germs: List[Germ]):
    dominant = max(germs, key=lambda x: x.num)
    total_num = sum(map(lambda x: x.num, germs))
    return Germ(dominant.row, dominant.col, dominant.d, total_num)


def crash(germs: List[Germ]):
    new_germs = []
    crashed = []
    num_germ = len(germs)
    for i in range(num_germ):
        if i not in crashed:
            crash_flag = False
            crash_germs = [germs[i]]
            for j in range(num_germ):
                if i != j:
                    if germs[i].loc == germs[j].loc:
                        crash_germs.append(germs[j])
                        crashed.append(j)
                        crash_flag = True
            if crash_flag:
                new_germs.append(crash_op(crash_germs))
            else:
                new_germs.append(germs[i])
    return new_germs


def simulation(germs: List[Germ], map_size):
    for germ in germs:
        germ.move(map_size)
    return crash(germs)


def summation(germs: List[Germ]):
    cnt = 0
    for germ in germs:
        cnt += germ.num
    return cnt


def print_map(germs, n):
    _map = zeros_list(n, n)
    for germ in germs:
        i, j = germ.loc()
        _map[i][j] += 1
    from pprint import pprint
    pprint(_map)
    return


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        n, m, k = tuple(map(int, input().rstrip().split(' ')))
        _germs = [list(map(int, input().rstrip().split(' '))) for _ in range(k)]
        germs = []
        for row, col, num, d in _germs:
            germs.append(Germ(row, col, DIRECTION[d], num))
        for _ in range(m):
            germs = simulation(germs, n)
            # print(len(germs))
            # print_map(germs, n)
        print('#%d %d' % (t+1, summation(germs)))
        # print_map(germs, n)


if __name__ == '__main__':
    main()
