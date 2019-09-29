"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu
보호필름
"""
from pprint import pprint


A = 0
B = 1
CELL = ['A', 'B']


def get_column(matrix, c):
    # x에 한 행 씩 들어가고 각 행의 column c 의 값을 가져와서 리스트로
    return list(map(lambda x: x[c], matrix))



def column_check(column, k):
    cnt = 1
    for j in range(1, len(column)):
        if column[j] == column[j-1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= k:
            return True
    return False


def check(film, k):
    for w in range(len(film[0])):
        if not column_check(get_column(film, w), k):
            return False
    return True


def print_film(film):
    print('==================================')
    for row in film:
        for e in row:
            print(CELL[e], end=' ')
        print()
    print('==================================')


def row_change(matrix, row_id, value):
    temp = []
    w = len(matrix[0])
    for r in range(len(matrix)):
        if row_id == r:
            temp.append([value for _ in range(w)])
        else:
            temp.append(matrix[r])
    return temp


def solution(film, k):
    """
    :param film: film matrix
    :param k: # pass injection
    :return: minimum injection
    """
    depth = len(film)
    # width = len(film[0])
    path = []

    def dfs(state, row, value, visited):
        new_state = row_change(state, row, value)       # film state update
        # print_film(state)
        visited = visited + [(row, value)]
        injected = list(map(lambda x: x[0], visited))   # 현재까지 투약한 층

        cnt = len(visited)

        if path:
            if len(path[0]) <= cnt:
                # 현재 path(cnt)가 기존 최소 path보다 크거나 같으면 탐색 중지
                return

        if check(new_state, k):
            if not path:
                path.append(visited)
            else:
                if len(path[0]) > len(visited):
                    path.pop()
                    path.append(visited)
            return

        if cnt >= k:
            # 투약 횟수가 통과기준 K 보다 크거나 같은데
            # pass를 못하면 더 이상 탐색 하지 않음
            return

        for r in range(depth):
            for v in [A, B]:
                if r not in injected:
                    # 현재까지 투약하지 않은 층에 대해서만
                    dfs(new_state, r, v, visited)

    if check(film, k):
        return 0
    else:
        for rr in range(2, depth):
            for vv in [A, B]:
                dfs(film, rr, vv, [])
        # print(path)
        return len(path[0])


def main():
    import time
    s = time.time()

    test_cases = int(input().rstrip())
    for t in range(test_cases):
        dd, ww, kk = list(map(int, input().rstrip().split(' ')))
        film = [list(map(int, input().rstrip().split())) for _ in range(dd)]
        # print('D=%d, W=%d, K=%d' % (dd, ww, kk))
        print('#%d %d' % (t+1, solution(film, kk)))
        # print('=================================================')

    print(time.time() - s)


if __name__ == '__main__':
    main()
