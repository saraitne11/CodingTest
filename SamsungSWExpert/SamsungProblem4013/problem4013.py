"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH
특이한 자석
"""
from pprint import pprint
from typing import List, Union

NUM_MAGNET = 4
MAGNET_TOOTH = 8
N = 0
S = 1

LF = 2
RF = 6


def chain_rotations(magnets, mg_id, d):
    rotations = [0 for _ in range(NUM_MAGNET)]
    rotations[mg_id] = d

    # right side chain rotation
    mg_cur = mg_id
    d_cur = d
    mg_right = mg_cur + 1
    while mg_right < NUM_MAGNET:
        if magnets[mg_right][RF] != magnets[mg_cur][LF]:
            rotations[mg_right] = -d_cur
            mg_cur = mg_right
            d_cur = -d_cur
            mg_right = mg_cur + 1
        else:
            break

    # left side chain rotation
    mg_cur = mg_id
    d_cur = d
    mg_left = mg_cur - 1
    while mg_left >= 0:
        if magnets[mg_left][LF] != magnets[mg_cur][RF]:
            rotations[mg_left] = -d_cur
            mg_cur = mg_left
            d_cur = -d_cur
            mg_left = mg_cur - 1
        else:
            break

    # print(rotations)
    for m, d in enumerate(rotations):
        rotate_magnets(magnets, m, d)
    return


def rotate_magnets(magnets: List[List[int]], mg_idx: int, d: int):
    magnets[mg_idx] = magnets[mg_idx][-d:] + magnets[mg_idx][:-d]


def score(magnets: List[List[int]]) -> int:
    s = 0
    heads = list(map(lambda x: x[0], magnets))  # 자석의 화살표 부분 날을 가져옴
    for i, p in enumerate(heads):
        if p == S:
            s += 2**i
    return s


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        num_rotate = int(input().rstrip())

        magnets = []
        for _ in range(NUM_MAGNET):
            m = list(map(int, input().rstrip().split(' ')))
            magnets.append(m)
        # magnets = [list(map(int, input().rstrip().split(' '))) for _ in range(NUM_MAGNET)]

        rotation = []
        for _ in range(num_rotate):
            r = tuple(map(int, input().rstrip().split(' ')))
            rotation.append(r)

        # print('=======================================')
        # print('test case %d' % t)
        # pprint(magnets)
        # print(rotation)
        # print('=======================================')
        for m, d in rotation:
            chain_rotations(magnets, m-1, d)

        print('#%d %d' % (t+1, score(magnets)))


if __name__ == '__main__':
    main()
