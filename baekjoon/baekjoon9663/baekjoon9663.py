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
    ans = []

    def search(points):
        if len(points) == n:
            ans.append(points)
            return

        next_row = points[-1][0] + 1
        candidates = [(next_row, j) for j in range(n)]

        for candi in candidates:
            promising = True

            for p in points:
                if is_catch(candi, p):
                    # print(candi, p)
                    promising = False
                    break

            if promising:
                new_points = points + [candi]
                search(new_points)
        return

    start_points = [(0, j) for j in range(n)]
    for start in start_points:
        search([start])
    return ans


def main():
    import time
    s = time.time()

    # n = int(input())
    for n in range(1, 12):
        ans = solution(n)
    # print(ans)
        print(len(ans))

    print(time.time() - s)


if __name__ == '__main__':
    main()
