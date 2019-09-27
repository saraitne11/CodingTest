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


def in_matrix(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False


def is_connected(current_tunnels, before_tunnel):
    if before_tunnel == UP and DOWN in current_tunnels:
        return True
    elif before_tunnel == DOWN and UP in current_tunnels:
        return True
    elif before_tunnel == RIGHT and LEFT in current_tunnels:
        return True
    elif before_tunnel == LEFT and RIGHT in current_tunnels:
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
    # mtx = [row for _ in range(m)]     모든 row가 같은 주소를 참조하게 되서 mtx[i][j]만 수정해도 mtx[i][:]가 바뀜
    return mtx


def bfs(tunnel_map, start_i, start_j, max_time):
    n = len(tunnel_map)
    m = len(tunnel_map[0])
    visit = zeros_list(n, m)

    cnt = 1
    visit[start_i][start_j] = 1
    queue = [(start_i, start_j, 1)]     # (행, 렬, 현재 이동 거리)

    while queue:
        cur = queue.pop(0)          # Dequeue
        i, j, t = cur
        tunnels = TUNNELS[tunnel_map[i][j]]
        for tunnel in tunnels:
            new_i = i + tunnel[0]
            new_j = j + tunnel[1]
            new_t = t + 1
            if in_matrix(new_i, new_j, n, m):       # 매트릭스 내부이며
                if tunnel_map[new_i][new_j] != 0:   # 이 위치에 터널이 있으며
                    new_tunnels = TUNNELS[tunnel_map[new_i][new_j]]
                    if is_connected(new_tunnels, tunnel):   # 터널이 연결되어 있고
                        if visit[new_i][new_j] == 0:        # 아직 방문 전이고
                            if new_t <= max_time:           # 최대 이동회수 이하
                                # 위의 4 조건을 모두 만족하면 방문 가능하므로
                                # 방문 표시하고 Inqueue
                                visit[new_i][new_j] = 1
                                queue.append((new_i, new_j, new_t))
                                cnt += 1
    # pprint(visit)
    return cnt


def main():
    test_cases = int(input().rstrip())
    for T in range(test_cases):
        N, M, R, C, L = list(map(int, input().rstrip().split(' ')))

        tunnel_map = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

        # print(N, M, R, C, L)
        # pprint(map_matrix)
        print('#%d %d' % (T+1, bfs(tunnel_map, R, C, L)))
        # break


if __name__ == '__main__':
    main()