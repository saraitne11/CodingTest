"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu
보호필름
"""
from pprint import pprint
from collections import deque


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
    depth = len(film)
    width = len(film[0])

    if check(film, k):
        return 0

    cnt = 1
    # queue = []
    queue = deque([])
    for d in range(depth):
        for v in [A, B]:
            new_film = row_change(film, d, v)
            if check(new_film, k):
                return cnt
            queue.append((new_film, [d], cnt))

    # print(list(map(lambda x: x[1:], queue)))

    while queue:
        # print(list(map(lambda x: x[1:], queue)))
        # cur_film, visited, cnt = queue.pop(0)
        cur_film, visited, cnt = queue.popleft()
        # print(visited, cnt)
        # print_film(cur_film)
        for d in range(depth):
            for v in [A, B]:
                if d not in visited:
                    new_cnt = cnt + 1
                    new_visited = visited+[d]

                    if new_cnt >= k:
                        return new_cnt

                    new_film = row_change(cur_film, d, v)
                    if check(new_film, k):
                        # print(new_visited)
                        # print_film(new_film)
                        return new_cnt
                    queue.append((new_film, new_visited, new_cnt))

    return -1


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
        # break

    print(time.time() - s)


if __name__ == '__main__':
    main()
