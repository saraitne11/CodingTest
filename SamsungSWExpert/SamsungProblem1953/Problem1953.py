"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq
탈주범 검거
"""

from pprint import pprint


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


TUNNELS = {1: (UP, DOWN, LEFT, RIGHT),
           2: (UP, DOWN),
           3: (LEFT, RIGHT),
           4: (UP, RIGHT),
           5: (DOWN, RIGHT),
           6: (LEFT, DOWN),
           7: (LEFT, UP)}


def is_in_matrix(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False


def is_connected(a, b, mtx):
    """
    :param a: (i1, j1)
    :param b: (i2, j2)
    :param mtx: matrix
    :return: True or False
    """
    a2b = False
    b2a = False
    route = TUNNELS[mtx[a[0]][a[1]]]
    for r in route:
        new_ = (a[0] + r[0], a[1] + r[1])
        if new_[0] == b[0] and new_[1] == b[1]:
            a2b = True
            break

    route = TUNNELS[mtx[b[0]][b[1]]]
    for r in route:
        new_ = (b[0] + r[0], b[1] + r[1])
        if new_[0] == a[0] and new_[1] == a[1]:
            b2a = True
            break

    if a2b and b2a:
        return True
    else:
        return False


def is_connected_2(current_move, before_move):
    if before_move == UP and DOWN in current_move:
        return True
    elif before_move == DOWN and UP in current_move:
        return True
    elif before_move == RIGHT and LEFT in current_move:
        return True
    elif before_move == LEFT and RIGHT in current_move:
        return True
    else:
        return False


def solution(matrix, start, move):
    n = len(matrix)
    m = len(matrix[0])
    destination = []

    def search(current, left_move):
        left_move -= 1
        i, j = current[0], current[1]

        if left_move == 0:
            if current not in destination:
                destination.append(current)
            return
        else:
            route = TUNNELS[matrix[i][j]]
            search((i, j), left_move)   # 이동하지 않고 시간 보내기
            for r in route:             # 연결된 터널로 이동
                new_i = i + r[0]
                new_j = j + r[1]
                if is_in_matrix(new_i, new_j, n, m) and matrix[new_i][new_j] > 0:
                    # if is_connected((i, j), (new_i, new_j), matrix):
                    if is_connected_2(TUNNELS[matrix[new_i][new_j]], r):
                        search((new_i, new_j), left_move)

    search(start, move)
    # print(destination)
    return len(destination)


def main():
    test_cases = int(input().rstrip())
    for T in range(test_cases):
        N, M, R, C, L = list(map(int, input().rstrip().split(' ')))

        map_matrix = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

        # print(N, M, R, C, L)
        # pprint(map_matrix)
        print(solution(map_matrix, (R, C), L))
        # break


if __name__ == '__main__':
    main()