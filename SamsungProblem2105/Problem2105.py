"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
디저트 카페
"""


MOVES = ((1, 1), (1, -1), (-1, -1), (-1, 1))


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


def search_route(matrix, start):
    route_idx = []
    route_val = []
    n = len(matrix)

    def dfs(cur, v_idx, v_val, move):
        """
        :param cur: current location (i, j)
        :param v_idx: visited indices [(i1, j1), (i2, j2), ...]
        :param v_val: visited values [v1, v2, v3, ...]
        :param move: current move direction one of (1, 1), (1, -1), (-1, -1), (-1, 1)
        """

        if is_in_matrix(cur[0], cur[1], n, n):          # 매트릭스 안쪽이면
            c_val = matrix[cur[0]][cur[1]]              # current value

            if cur != start and c_val in v_val:
                # 출발 노드가 아니면서 현재 값이 방문한 값들에 있으면
                # 중복이므로 바로 리턴
                return
            v_val = v_val + [c_val]
            v_idx = v_idx + [cur]

            if move == MOVES[3]:                            # 우상단 방향
                if cur == start:                        # 현재 노드가 출발 노드면 리턴
                    route_idx.append(v_idx[:-1])
                    route_val.append(v_val[:-1])
                    # route_idx.append(idx)
                    # route_val.append(val)
                    return
                else:                                       # 현재 노드가 출발 노드가 아니면,
                    next_ = (cur[0] + move[0], cur[1] + move[1])
                    dfs(next_, v_idx, v_val, move)               # 같은 방향으로 다시 dfs

            elif move == MOVES[2]:                          # 좌상단 방향
                next_ = (cur[0] + move[0], cur[1] + move[1])    # 같은 방향 dfs
                dfs(next_, v_idx, v_val, move)
                new_move = MOVES[3]                                 # 다음 우상단 방향 dfs
                next_ = (cur[0] + new_move[0], cur[1] + new_move[1])
                dfs(next_, v_idx, v_val, new_move)

            elif move == MOVES[1]:                          # 좌하단 방향
                next_ = (cur[0] + move[0], cur[1] + move[1])    # 같은 방향 dfs
                dfs(next_, v_idx, v_val, move)
                new_move = MOVES[2]                                 # 다음 좌상단 방향 dfs
                next_ = (cur[0] + new_move[0], cur[1] + new_move[1])
                dfs(next_, v_idx, v_val, new_move)

            elif move == MOVES[0]:                          # 우하단 방향
                next_ = (cur[0] + move[0], cur[1] + move[1])    # 같은 방향 dfs
                dfs(next_, v_idx, v_val, move)
                new_move = MOVES[1]                                 # 다음 좌하단 방향 dfs
                next_ = (cur[0] + new_move[0], cur[1] + new_move[1])
                dfs(next_, v_idx, v_val, new_move)
            else:
                print('???', v_idx)
        else:
            return

    dfs(start, [], [], MOVES[0])
    return route_idx, route_val


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        n = int(input().rstrip())
        cafes = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]

        # print('#%d %d' % (t+1, 0))
        # print(n)
        # print(cafes)
        routes = []
        values = []
        for i in range(n-1):
            for j in range(1, n-1):
                r, v = search_route(cafes, (i, j))
                # print(r)
                # print(v)
                routes.extend(r)
                values.extend(v)
        # print(values)
        # print(max(values, key=len))

        if values:
            ans = len(max(values, key=len))
        else:
            ans = -1
        print('#%d %d' % (t+1, ans))


if __name__ == '__main__':
    main()
