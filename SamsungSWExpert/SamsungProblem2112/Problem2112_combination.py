"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu
보호필름
"""
# from pprint import pprint
from itertools import combinations, product


MEDICINE = [0, 1]   # [A, B]
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


def row_changes(matrix, row_id, value):
    if len(row_id) != len(value):
        raise ValueError("len(row_id) %d  not equal len(value) %d" % (len(row_id), len(value)))
    w = len(matrix[0])
    temp = []
    c = 0
    for r in range(len(matrix)):
        if c >= len(row_id) or r != row_id[c]:
            temp.append(matrix[r])
        else:
            temp.append([value[c] for _ in range(w)])
            c += 1
    return temp


def print_film(film):
    for row in film:
        for e in row:
            print(CELL[e], end=' ')
        print()


def solution(film, dd, kk):

    cnt = 0
    if check(film, kk):
        return cnt

    while True:
        cnt += 1
        if cnt == kk:   # 투약 횟수와 통과기준 k가 같다면 투약 횟수 바로 리턴
            return cnt

        m_combi = list(product(MEDICINE, repeat=cnt))
        f_combi = list(combinations(list(range(dd)), r=cnt))
        # print(cnt)
        # print(f_combi)
        # print(m_combi)
        for f in f_combi:
            for m in m_combi:
                # tt = row_changes(film, f, m)
                # print(f, m)
                # print_film(tt)
                if check(row_changes(film, f, m), kk):
                    return cnt


def main():
    import time
    s = time.time()

    test_cases = int(input().rstrip())
    for t in range(test_cases):
        dd, ww, kk = list(map(int, input().rstrip().split(' ')))
        film = [list(map(int, input().rstrip().split())) for _ in range(dd)]
        # print('D=%d, W=%d, K=%d' % (dd, ww, kk))
        # print_film(film)
        print('#%d %d' % (t+1, solution(film, dd, kk)))
        # print('=================================================')

    print(time.time() - s)


if __name__ == '__main__':
    main()
