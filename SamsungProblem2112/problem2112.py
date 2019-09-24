"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu
보호필름
"""
import re
from pprint import pprint
from typing import List, Tuple, Iterable
from copy import deepcopy
from itertools import combinations, product


MEDICINE = [0, 1]   # [A, B]
CELL = ['A', 'B']


def get_column(matrix: List[List[int]], c: int):
    # x에 한 행 씩 들어가고 각 행의 column c 의 값을 가져와서 리스트로
    return list(map(lambda x: x[c], matrix))


def check(film, ww, kk):
    a = re.compile('0{%d,}' % kk)
    b = re.compile('1{%d,}' % kk)
    for w in range(ww):
        col = ''.join(map(str, get_column(film, w)))
        a_continue = a.findall(col)
        b_continue = b.findall(col)
        if a_continue or b_continue:
            pass
        else:
            return False
    return True


def row_changes(matrix: List[List[int]], row_id: Tuple, value: Tuple):
    temp = deepcopy(matrix)         # Do not touch original data
    if len(row_id) != len(value):
        raise ValueError("len(row_id) %d  not equal len(value) %d" % (len(row_id), len(value)))

    for r, v in zip(row_id, value):
        temp[r] = [v for _ in temp[r]]
    return temp


def print_film(film):
    for row in film:
        for e in row:
            print(CELL[e], end=' ')
        print()


def solution(film, dd, ww, kk):
    cnt = 0
    if check(film, ww, kk):
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
                # if check(row_changes(film, f, m), ww, kk):
                if check(row_changes(film, f, m), ww, kk):
                    return cnt


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        dd, ww, kk = list(map(int, input().rstrip().split(' ')))
        film = [list(map(int, input().rstrip().split())) for _ in range(dd)]
        # print('D=%d, W=%d, K=%d' % (dd, ww, kk))
        # print_film(film)
        print('#%d %d' % (t+1, solution(film, dd, ww, kk)))
        # print('=================================================')


if __name__ == '__main__':
    main()
