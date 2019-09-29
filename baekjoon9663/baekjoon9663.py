"""
N-Queen 문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
"""


def is_catch(a, b):
    """
    :param a: tuple or list (i1, j1)
    :param b: tuple or list(i2, j2)
    :return: True or False
    """
    if a[0] == b[0]:        # same row
        return True
    elif a[1] == b[1]:      # same column
        return True
    elif abs(a[0]-b[0]) == abs(a[1]-b[1]):  # diagonal
        return True
    else:
        return False


def solution(n):



def main():
    n = int(input())


if __name__ == '__main__':
    main()