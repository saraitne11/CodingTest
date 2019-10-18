"""
파이썬 SW문제해결 응용_구현 - 02 완전 검색
5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
"""


def dfs(g, n, start):
    min_val = [999999]

    def search(current, cum_val, remain):

        if not remain:
            cum_val = cum_val + g[current][0]   # (0,0)로 복귀
            if min_val[0] > cum_val:
                min_val[0] = cum_val
            return

        else:
            for new_c in remain:
                new_v = cum_val + g[current][new_c]
                if new_v < min_val[0]:
                    new_r = remain[:]
                    new_r.remove(new_c)
                    search(new_c, new_v, new_r)

    search(start, 0, list(range(1, n)))

    return min_val[0]


def main():
    test_case = int(input().rstrip())
    for t in range(test_case):
        n = int(input().rstrip())
        g = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
        # print(n)
        # print(g)
        print('#%d %d' % (t+1, dfs(g, n, 0)))


if __name__ == '__main__':
    main()
