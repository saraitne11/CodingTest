"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu
보호필름
"""
import re
from pprint import pprint
from typing import List
from copy import deepcopy


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


def row_change(matrix, row_id, value):
    matrix[row_id] = [value for _ in matrix[row_id]]


def search(film, dd, ww, kk):

    cnt = 0
    while True:
        if check(film, ww, kk):
            return cnt
        cnt += 1
        film_temp = deepcopy(film)
        for d in range(dd):
            row_change(film_temp, d, 0)     # A 약품
            row_change(film_temp, d, 1)     # B 약품


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        dd, ww, kk = list(map(int, input().rstrip().split(' ')))
        film = [list(map(int, input().rstrip().split())) for _ in range(dd)]
        print('Test Case %d' % (t+1))
        # print(dd, ww, kk)
        # pprint(film)
        print(check(film, kk))


if __name__ == '__main__':
    main()
