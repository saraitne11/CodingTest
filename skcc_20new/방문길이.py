import numpy as np


def solution(dirs):
    answer = 0
    i = 5
    j = 5
    mtx = np.zeros([11, 11, 11, 11], dtype=np.uint8)

    for d in dirs:
        if d == 'U':
            ni = i
            nj = j + 1
        elif d == 'D':
            ni = i
            nj = j - 1
        elif d == 'L':
            ni = i - 1
            nj = j
        elif d == 'R':
            ni = i + 1
            nj = j
        else:
            print("input error - %s" % d)
            return -1

        if 0 <= ni < 11 and 0 <= nj < 11:
            if mtx[i][j][ni][nj] != 1 and mtx[ni][nj][i][j] != 1:
                mtx[i][j][ni][nj] = 1
                mtx[ni][nj][i][j] = 1
                answer += 1
            i = ni
            j = nj

    return answer


if __name__ == '__main__':
    print(solution('LULLLLLLU'))
