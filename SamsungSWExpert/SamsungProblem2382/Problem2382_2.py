"""
미생물 격리
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl
"""

from typing import List

DIRECTION = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}


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


class State(object):
    def __init__(self, size, germs: List[Germ]):
        self.size = size
        self.map = {(i, j): [] for i in range(size) for j in range(size)}
        self.germs = germs
        for germ in self.germs:
            i, j = germ.loc
            self.map[(i, j)].append(germ)

    def simulate(self):
        for germ in self.germs:
            i, j = germ.loc
            self.map[(i, j)].remove(germ)
            germ.move(self.size)
            i, j = germ.loc
            self.map[(i, j)].append(germ)

        self.germs = []
        for key, value in self.map.items():
            if len(value) > 1:
                crashed = crash_op(value)
                self.map[key] = [crashed]
                self.germs.append(crashed)
            elif len(value) == 1:
                self.germs.extend(value)
            else:
                pass

    def get_total(self):
        cnt = 0
        for germ in self.germs:
            cnt += germ.num
        return cnt


def crash_op(germs: List[Germ]):
    dominant = max(germs, key=lambda x: x.num)
    total_num = sum(map(lambda x: x.num, germs))
    return Germ(dominant.row, dominant.col, dominant.d, total_num)


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        n, m, k = tuple(map(int, input().rstrip().split(' ')))
        _germs = [list(map(int, input().rstrip().split(' '))) for _ in range(k)]
        germs = []
        for row, col, num, d in _germs:
            germs.append(Germ(row, col, DIRECTION[d], num))
        state = State(n, germs)
        for _ in range(m):
            state.simulate()
        print('#%d %d' % (t+1, state.get_total()))


if __name__ == '__main__':
    main()
